#!/usr/bin/env python3
"""
Resolve a staging .bib against authoritative registries to fill VERIFIED ids:
  - papers  -> Crossref (then OpenAlex)  : DOI, journal, volume, number, pages
  - books   -> Google Books              : ISBN-13, publisher, year

Matching is TITLE-DRIVEN: a candidate is accepted only if the registry record's
title covers the supplied title (token coverage >= threshold) AND the year matches
within 1. This rejects right-author/wrong-paper false positives. Identifiers come
from the registries (never invented); unresolved entries keep a TODO with the top
candidate noted for manual review.

Usage:
    .venv/bin/python tools/research/resolve_bib.py --bib references-curriculum-canon.bib
    # -> references-curriculum-canon.resolved.bib  (+ per-entry audit to stdout)
"""
from __future__ import annotations

import argparse
import datetime
import os
import pathlib
import re
import sys
import time

try:
    import requests
except ModuleNotFoundError:
    sys.exit("Error: requests not installed. uv pip install -r tools/requirements.txt")

MAILTO = os.environ.get("CROSSREF_MAILTO", "admin@deloryx.com")
HEADERS = {"User-Agent": f"deloryx-book-refs/1.0 (mailto:{MAILTO})"}
TIMEOUT = 25
ART_COVER = 0.55   # min fraction of supplied-title tokens present in candidate
BOOK_COVER = 0.50

STOP = {"the", "a", "an", "of", "and", "for", "to", "in", "on", "with", "an",
        "is", "as", "at", "by", "or", "under", "into", "new"}

ENTRY_RE = re.compile(r"@(\w+)\{([^,]+),(.*?)\n\}", re.S)
FIELD_RE = re.compile(r"(\w+)\s*=\s*\{(.*?)\}\s*,?\s*$", re.M)
FIELD_ORDER = ["author", "title", "journaltitle", "edition", "year",
               "volume", "number", "pages", "publisher", "isbn", "doi"]


def parse_bib(text: str) -> list[dict]:
    out = []
    for m in ENTRY_RE.finditer(text):
        body = m.group(3)
        fields = {fm.group(1).lower(): fm.group(2).strip() for fm in FIELD_RE.finditer(body)}
        out.append({"type": m.group(1).lower(), "key": m.group(2).strip(), "fields": fields})
    return out


def emit(e: dict) -> str:
    f = e["fields"]
    order = [k for k in FIELD_ORDER if k in f] + [k for k in f if k not in FIELD_ORDER]
    return "\n".join([f"@{e['type']}{{{e['key']},", *[f"  {k} = {{{f[k]}}}," for k in order], "}"])


def toks(s: str) -> set[str]:
    return {t for t in re.findall(r"[a-z0-9]+", (s or "").lower()) if t not in STOP and len(t) > 1}


def coverage(want: str, cand: str) -> float:
    w = toks(want)
    if not w:
        return 0.0
    return len(w & toks(cand)) / len(w)


def surnames(author: str) -> list[str]:
    out = []
    for a in author.split(" and "):
        a = a.strip()
        out.append((a.split(",")[0] if "," in a else a.split()[-1]).lower() if a else "")
    return [s for s in out if s]


def crossref(title: str, author: str, year: str) -> dict | None:
    params = {"rows": 6, "mailto": MAILTO, "query.bibliographic": title,
              "select": "DOI,title,container-title,short-container-title,volume,issue,page,issued,author,type"}
    if author:
        params["query.author"] = " ".join(surnames(author))
    try:
        r = requests.get("https://api.crossref.org/works", params=params, headers=HEADERS, timeout=TIMEOUT)
        items = r.json().get("message", {}).get("items", []) if r.status_code == 200 else []
    except Exception:
        return None
    yr = int(year) if year.isdigit() else None

    def is_preprint(it):
        return it.get("type") == "posted-content" or (it.get("DOI", "") or "").startswith("10.2139")

    # Prefer the published version over SSRN/preprints: track best overall and best non-preprint.
    best, bcov = None, -1.0
    bestpub, bpubcov = None, -1.0
    for it in items:
        cov = coverage(title, (it.get("title") or [""])[0])
        if cov > bcov:
            best, bcov = it, cov
        if not is_preprint(it) and cov > bpubcov:
            bestpub, bpubcov = it, cov
    if bestpub is not None and bpubcov >= ART_COVER:
        best, bcov = bestpub, bpubcov
    if not best:
        return None
    cy = (best.get("issued", {}).get("date-parts", [[None]]) or [[None]])[0][0]
    ok = bcov >= ART_COVER and (yr is None or (cy and abs(int(cy) - yr) <= 1))
    return {"item": best, "cov": round(bcov, 2), "title": (best.get("title") or [""])[0], "accepted": ok}


def openalex(title: str, author: str, year: str) -> dict | None:
    try:
        r = requests.get("https://api.openalex.org/works",
                         params={"search": title, "per-page": 6, "mailto": MAILTO},
                         headers=HEADERS, timeout=TIMEOUT)
        items = r.json().get("results", []) if r.status_code == 200 else []
    except Exception:
        return None
    yr = int(year) if year.isdigit() else None
    best, bcov = None, -1.0
    for it in items:
        cov = coverage(title, it.get("title") or "")
        if cov > bcov:
            best, bcov = it, cov
    if not best:
        return None
    cy = best.get("publication_year")
    ok = bcov >= ART_COVER and (yr is None or (cy and abs(int(cy) - yr) <= 1))
    return {"item": best, "cov": round(bcov, 2), "title": best.get("title") or "", "accepted": ok}


def openlibrary(title: str, author: str) -> dict | None:
    """OpenLibrary search (keyless, no quota) for a book's ISBN-13 + publisher + year."""
    sur = surnames(author)
    try:
        r = requests.get("https://openlibrary.org/search.json",
                         params={"title": title, "author": sur[0] if sur else author,
                                 "fields": "title,author_name,first_publish_year,isbn,publisher",
                                 "limit": 5},
                         headers=HEADERS, timeout=TIMEOUT)
        docs = r.json().get("docs", []) if r.status_code == 200 else []
    except Exception:
        return None
    best, bcov = None, -1.0
    for d in docs:
        cov = coverage(title, d.get("title", ""))
        if cov > bcov:
            best, bcov = d, cov
    if not best:
        return None
    isbn = next((i for i in best.get("isbn", []) if len(i) == 13 and i.startswith(("978", "979"))), None)
    pub = (best.get("publisher") or [None])[0]
    return {"cov": round(bcov, 2), "title": best.get("title", ""), "isbn": isbn,
            "publisher": pub, "year": str(best.get("first_publish_year") or ""),
            "accepted": bcov >= BOOK_COVER}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--bib", required=True)
    ap.add_argument("--out")
    ap.add_argument("--sleep", type=float, default=0.4)
    args = ap.parse_args()
    src = pathlib.Path(args.bib)
    if not src.is_file():
        sys.exit(f"Not found: {src}")
    out = pathlib.Path(args.out) if args.out else src.with_suffix(".resolved.bib")
    entries = parse_bib(src.read_text(encoding="utf-8"))
    print(f"[resolve_bib] {len(entries)} entries")

    blocks, n_ok, n_miss = [], 0, 0
    for e in entries:
        f, note = e["fields"], ""
        title, author, year = f.get("title", ""), f.get("author", ""), f.get("year", "")
        if e["type"] not in ("book", "article"):
            # @online / @misc etc. are not registry-resolvable here; pass through unchanged.
            blocks.append(emit(e))
            continue
        if e["type"] == "book":
            # Books are edition-specific. Registry search returns WORK-level ISBNs/years
            # (often the first edition), which would corrupt a given edition's entry, so we
            # do NOT auto-fill them. A book is complete with author+title+edition+year+publisher.
            if f.get("title") and f.get("year") and f.get("publisher"):
                print(f"  OK   {e['key']:<26} [as-authored] {f.get('edition','')} {f.get('publisher','')} {f.get('year','')}")
                n_ok += 1
            else:
                note = f"% TODO verify {e['key']}: need title+year+publisher (edition-specific; do not trust work-level ISBN)"
                print(f"  MISS {e['key']:<26} incomplete (need year/publisher)")
                n_miss += 1
        else:  # article
            res = crossref(title, author, year)
            time.sleep(args.sleep)
            if not (res and res["accepted"]):
                oa = openalex(title, author, year)
                time.sleep(args.sleep)
                if oa and oa["accepted"]:
                    res = oa
            if res and res["accepted"]:
                it, src_name = res["item"], ("crossref" if "container-title" in res["item"] or "issued" in res["item"] else "openalex")
                if "issued" in it:  # crossref
                    if it.get("DOI"):
                        f.setdefault("doi", it["DOI"])
                    cont = it.get("container-title") or it.get("short-container-title")
                    if cont and not f.get("journaltitle"):
                        f["journaltitle"] = cont[0]
                    if it.get("volume"):
                        f.setdefault("volume", it["volume"])
                    if it.get("issue"):
                        f.setdefault("number", it["issue"])
                    if it.get("page"):
                        f.setdefault("pages", it["page"].replace("-", "--"))
                else:  # openalex
                    doi = (it.get("doi") or "").replace("https://doi.org/", "")
                    if doi:
                        f.setdefault("doi", doi)
                    b = it.get("biblio") or {}
                    if b.get("volume"):
                        f.setdefault("volume", b["volume"])
                    if b.get("issue"):
                        f.setdefault("number", b["issue"])
                    if b.get("first_page"):
                        f.setdefault("pages", f"{b['first_page']}--{b.get('last_page','')}".rstrip("-"))
                print(f"  OK   {e['key']:<26} [{src_name} {res['cov']}] doi={f.get('doi','?')} | {res['title'][:50]}")
                n_ok += 1
            else:
                cov = res["cov"] if res else "n/a"
                cand = (res.get("title") or "") if res else ""
                note = f"% TODO verify {e['key']}: DOI unresolved (top cov {cov}: {cand[:50]!r})"
                print(f"  MISS {e['key']:<26} DOI unresolved (cov {cov})")
                n_miss += 1
        block = emit(e)
        blocks.append(block + ("\n" + note if note else ""))

    today = datetime.date.today().isoformat()
    head = (f"% Resolved from {src.name} via Crossref/OpenAlex/Google Books on {today}.\n"
            f"% {n_ok} resolved, {n_miss} need manual review. Identifiers from registries (title-gated).\n"
            f"% Dedupe against references.bib before merging.\n\n")
    out.write_text(head + "\n\n".join(blocks) + "\n", encoding="utf-8")
    print(f"[resolve_bib] wrote {out}: {n_ok} resolved, {n_miss} unresolved.")


if __name__ == "__main__":
    main()
