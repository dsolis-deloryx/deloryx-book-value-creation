#!/usr/bin/env python3
"""
Resolve the opaque Google grounding-redirect URLs in a Deep Research brief into
CANONICAL first-party documentation URLs, then emit @online BibLaTeX entries for
the official ones (Google / Meta help & developer docs).

Deep Research citations look like
  https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQ...
which 30x-redirect to the real page. This follows each redirect over HTTP, keeps
only first-party vendor domains, fetches the page <title>, and writes ready-to-paste
@online entries (url = canonical, urldate = today). Non-official sources are dropped.

Usage:
    .venv/bin/python tools/research/resolve_urls.py --infile research/paid-acquisition-platforms.md
    # -> references-paid-acquisition-platforms.bib
"""
from __future__ import annotations

import argparse
import datetime
import pathlib
import re
import sys
import time

try:
    import requests
except ModuleNotFoundError:
    sys.exit("Error: requests not installed. uv pip install -r tools/requirements.txt")

UA = "Mozilla/5.0 (X11; Linux x86_64) deloryx-book-refs/1.0"
HEADERS = {"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9"}
TIMEOUT = 25
REDIRECT_RE = re.compile(r"https://vertexaisearch\.cloud\.google\.com/grounding-api-redirect/[A-Za-z0-9_\-]+")

# domain -> (organization, citation-key prefix). Only these are emitted.
OFFICIAL = {
    "support.google.com": ("Google Help", "ghelp"),
    "developers.google.com": ("Google for Developers", "gdev"),
    "ads.google.com": ("Google Ads", "gads"),
    "business.google.com": ("Google", "gbiz"),
    "developers.facebook.com": ("Meta for Developers", "metadev"),
    "www.facebook.com": ("Meta Business Help Center", "metahelp"),
    "business.facebook.com": ("Meta Business Help Center", "metahelp"),
    "about.meta.com": ("Meta", "meta"),
    "www.meta.com": ("Meta", "meta"),
}


def org_for(host: str, path: str) -> tuple[str, str] | None:
    if host in OFFICIAL:
        org, pre = OFFICIAL[host]
        if host == "support.google.com" and path.startswith("/analytics"):
            return ("Google Analytics Help", "ga")
        if host == "support.google.com" and path.startswith("/google-ads"):
            return ("Google Ads Help", "gads")
        if host == "www.facebook.com" and "/business/help" not in path:
            return None  # only the business help center, not random fb pages
        return (org, pre)
    return None


def fetch_title(url: str) -> str | None:
    try:
        r = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        m = re.search(r"<title[^>]*>(.*?)</title>", r.text, re.S | re.I)
        if m:
            t = re.sub(r"\s+", " ", m.group(1)).strip()
            # strip trailing site suffixes
            for sep in (" - Google Ads Help", " - Google Analytics Help", " | Meta", " - Meta for Developers"):
                t = t.replace(sep, "")
            return t
    except Exception:
        return None
    return None


def keyize(prefix: str, url: str) -> str:
    m = re.search(r"/answer/(\d+)", url) or re.search(r"/(\d{6,})", url)
    if m:
        return f"{prefix}{m.group(1)}"
    slug = re.sub(r"[^a-z0-9]+", "-", url.rsplit("/", 1)[-1].lower()).strip("-")[:24] or "doc"
    return f"{prefix}-{slug}"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--infile", required=True)
    ap.add_argument("--out")
    ap.add_argument("--sleep", type=float, default=0.3)
    args = ap.parse_args()

    infile = pathlib.Path(args.infile)
    if not infile.is_file():
        sys.exit(f"Not found: {infile}")
    text = infile.read_text(encoding="utf-8")
    redirects = sorted(set(REDIRECT_RE.findall(text)))
    print(f"[resolve_urls] {len(redirects)} grounding-redirect URLs found")

    today = datetime.date.today().isoformat()
    seen: dict[str, dict] = {}
    dropped = 0
    for i, rdir in enumerate(redirects, 1):
        try:
            resp = requests.get(rdir, headers=HEADERS, timeout=TIMEOUT, allow_redirects=True)
            final = resp.url
        except Exception as e:
            print(f"  [{i}] redirect failed: {type(e).__name__}")
            continue
        time.sleep(args.sleep)
        m = re.match(r"https?://([^/]+)(/[^?#]*)", final)
        if not m:
            continue
        host, path = m.group(1), m.group(2)
        meta = org_for(host, path)
        if not meta:
            dropped += 1
            continue
        canonical = f"https://{host}{path}".rstrip("/")
        if canonical in seen:
            continue
        org, pre = meta
        title = fetch_title(final) or ""
        time.sleep(args.sleep)
        seen[canonical] = {"org": org, "key": keyize(pre, canonical), "title": title}
        print(f"  OK  {canonical}  | {title[:50]}")

    # de-dupe keys
    used = set()
    entries = []
    for url, d in sorted(seen.items()):
        key = d["key"]
        n = 2
        while key in used:
            key = f"{d['key']}-{n}"; n += 1
        used.add(key)
        title = d["title"] or "TODO TITLE"
        todo = "" if d["title"] else "\n  % TODO verify title (page may be JS-rendered)"
        entries.append(
            f"@online{{{key},\n"
            f"  author       = {{{{{d['org']}}}}},\n"
            f"  title        = {{{title}}},\n"
            f"  year         = {{2026}},\n"
            f"  url          = {{{url}}},\n"
            f"  urldate      = {{{today}}},\n"
            f"  organization = {{{d['org']}}},{todo}\n"
            f"}}"
        )

    out = pathlib.Path(args.out) if args.out else pathlib.Path(f"references-{infile.stem}.bib")
    head = (f"% Official-doc @online entries resolved from {infile.name} on {today}.\n"
            f"% Grounding redirects followed to canonical URLs; non-official domains dropped\n"
            f"% ({dropped} dropped). Verify each URL + title before merging into references.bib.\n\n")
    out.write_text(head + "\n\n".join(entries) + "\n", encoding="utf-8")
    print(f"[resolve_urls] wrote {out}: {len(entries)} official @online entries, {dropped} non-official dropped.")


if __name__ == "__main__":
    main()
