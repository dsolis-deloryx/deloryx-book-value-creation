<!-- Deep Research: agent=deep-research-max-preview-04-2026; interaction=v1_ChdDVW9XYXR6VURKNjBrZFVQdmNya2lBbxIXQ1VvV2F0elVESjYwa2RVUHZjcmtpQW8; steps=2; generated=2026-05-27 -->

*Disclaimer: The content of this report involves financial valuation mechanics, complex corporate finance structuring, and binding legal agreements. It is provided for informational and academic purposes only and does not constitute professional, financial, investment, tax, or legal advice. Consult licensed professionals before executing any binding term sheets or financial contracts.*

# Venture Finance and Startup Fundraising: A Comprehensive 2026 Practitioner's Guide

### Executive Summary
This definitive research brief synthesizes the structural and quantitative realities of venture capital fundraising as of mid-2026. Following the macroeconomic realignments of the post-pandemic era, venture capital has strictly prioritized operational efficiency and structural discipline over unconstrained growth. This summary outlines the core components necessary for practitioner fluency:
*   **Cap Tables & Ownership:** The capitalization table serves as the central ledger of equity ownership. In 2026, the logistical execution of these tables is overwhelmingly managed by specialized platforms (e.g., Carta, Pulley) that track Fully Diluted Shares Outstanding (FDSO) and complex option pool dynamics.
*   **Valuation Mechanics:** Valuations are bifurcated into Pre-Money (before investment) and Post-Money (after investment), determining the precise price per share paid by incoming investors.
*   **Early-Stage Instruments (SAFEs & Notes):** Pre-priced rounds rely heavily on Y Combinator Post-Money SAFEs and Convertible Notes. While notes act as debt with maturity dates and compounding interest, Post-Money SAFEs are fixed-equity contracts that explicitly shift compounding dilution onto founders.
*   **Priced Rounds & Legal Frameworks:** Standard institutional rounds (e.g., Series A, where median pre-money valuations hit $49.3 million in Q3 2025) are governed by National Venture Capital Association (NVCA) model documents, recently updated to address strict national data security and outbound investment regulations.
*   **Downside Protection:** Investors secure downside risk via 1x Non-Participating Liquidation Preferences (the market standard to prevent double-dipping) and Broad-Based Weighted Average Anti-Dilution provisions, which tempered the widespread down rounds seen in recent years.
*   **Runway & Investor Metrics:** Valuation multiples have recalibrated. Success in 2026 is determined by Net Revenue Retention (NRR), the Rule of 40, and strictly managed Burn Multiples (with a penalty for multiples exceeding 2.0x resulting in severe valuation haircuts). 

*   **Valuation paradigms have structurally shifted:** As of 2026, venture capital has decisively moved away from the "growth-at-all-costs" era, heavily recalibrating toward capital efficiency, with Net Revenue Retention (NRR) and the Burn Multiple serving as the primary arbiters of startup valuations.
*   **Standardized legal frameworks dominate:** Early-stage deals rely almost entirely on the Y Combinator Post-Money Simple Agreement for Future Equity (SAFE), while priced rounds are strictly governed by National Venture Capital Association (NVCA) model documents, which were notably updated in late 2025 to address national security and data regulations.
*   **Incomplete contracting theory drives deal structures:** The allocation of cash flow rights (e.g., liquidation preferences) is deliberately decoupled from control rights (e.g., board seats and voting vetoes) to align incentives under conditions of extreme uncertainty.
*   *Note on data fidelity:* While legal mechanics are canonized in public templates, contemporary valuation multiples and operational benchmarks rely on self-reported, secondary market aggregators; therefore, precise metrics should be viewed as reliable estimates rather than audited certainties.

The venture capital ecosystem operates at the intersection of high-risk financial contracting, operational scaling, and intense legal negotiation. To navigate this environment, practitioners must understand not only the raw mechanics of equity distribution but also the underlying economic theories that dictate investor behavior. Academic literature, most notably the foundational work of Steven N. Kaplan and Per Strömberg (published in *The Review of Economic Studies*, DOI: 10.1111/1467-937X.00245), demonstrates that real-world venture contracts are uniquely designed to separately allocate cash flow rights, board rights, and liquidation rights depending on a startup's financial performance [cite: 1, 2, 3, 4]. This separation mitigates the inherent information asymmetry between founders and investors.

Following the macroeconomic realignments of 2023 and 2024, the venture market in 2026 presents a disciplined environment. The focus has shifted from unchecked capital deployment to rigorous operational scrutiny. This report synthesizes the core mechanics, legal structures, and quantitative metrics that define startup fundraising today, providing a highly rigorous brief for graduate-level study and professional application.

```json
{
  "concept": "A vertical bar chart illustrating the resurgence of U.S. venture fundraising from 2023 to 2025, highlighting the leap in total capital deployed across private markets.",
  "reasoning_for_value": "While the text discusses a stabilized 2026 venture environment, providing the explicit Carta data for the 2023-2025 capital volume jump is essential for the reader to contextualize the scale of market recovery. Visualizing the billions raised emphasizes the structural shift.",
  "title": "Venture Capital Fundraising Rebounds Sharply in 2024 and 2025",
  "visual_type": "Vertical Bar Chart",
  "generation_method": "CODE",
  "justification_of_choice": "A vertical bar chart is the optimal format to compare straightforward, sequential annual totals. Alternatives considered were line charts (too few data points to form a meaningful trend line) and pie charts (inappropriate for longitudinal volume data). The bar chart emphasizes the magnitude of the year-over-year recovery.",
  "caption": "Total capital raised by startups on the Carta platform, demonstrating a clear resurgence following the 2022-2023 post-pandemic contraction.",
  "data_specification": {
    "source_snippets_ids": [64, 65],
    "data_structure": "An array of objects featuring 'Year' and 'Capital Raised ($B)'. Data points: 2023 ($75.1B inferred from 2024 18.4% jump), 2024 ($89.0B), 2025 ($119.5B).",
    "mapping": "X-axis: Year. Y-axis: Capital Raised ($B). Use a single focal color for all bars to indicate a continuous metric."
  },
  "design_and_interaction": {
    "layout": "Standard vertical orientation, Y-axis scaled from 0 to 140. Include data labels on top of each bar.",
    "aesthetics": {
      "style": "Professional & Corporate",
      "color_palette": "Background: White (#FFFFFF). Bars: Google Blue (#1A73E8). Text: Near-Black (#111111).",
      "additional_details": "Clean grid lines on the Y-axis."
    },
    "interactivity": "Tooltip on hover showing the exact billion dollar figure and year-over-year percentage increase.",
    "animation": "Static visual with no animation."
  }
}
```

## 1. Key Concepts in Venture Finance

To effectively execute a venture transaction, founders and investors must master a specialized lexicon and a set of core mechanics that govern ownership, control, and downside protection.

### Capitalization Tables and Ownership Dilution

The **capitalization table** (cap table) is the centralized, definitive ledger of a startup's ownership. It details every class of stock, option, warrant, and convertible security issued by the company. Understanding the cap table requires distinguishing between *authorized shares* (the total number of shares a corporate charter permits the company to issue) and *issued and outstanding shares* (the shares actually granted to stakeholders). In 2026, the logistical execution of capitalization tables is predominantly managed via specialized equity management platforms such as Carta or Pulley, which transition the ledger from static spreadsheets to dynamic, compliance-ready software [cite: 5, 6].

Dilution is the mathematical reality of raising capital: as a company issues new shares to investors, the relative ownership percentage of existing shareholders decreases. While the pie grows larger, each individual's slice represents a smaller fraction of the whole. A critical dynamic in venture fundraising is the concept of the **Fully Diluted Shares Outstanding (FDSO)**, which calculates ownership assuming every single option, warrant, and convertible security is exercised and converted into common stock.

A fundamental mechanism of dilution during a priced round is the creation or expansion of the employee option pool—a reserve of equity used to attract and retain future talent. As detailed by Brad Feld and Jason Mendelson in their authoritative text *Venture Deals: Be Smarter Than Your Lawyer and Venture Capitalist* (4th Edition, 2019, Wiley, ISBN 9781119594826), this dynamic often results in the "Option Pool Shuffle" [cite: 7, 8, 9].

**The Option Pool Shuffle**

Venture capitalists typically require that the employee option pool be expanded *prior* to their investment, meaning the dilution from this expansion falls entirely on the founders and early employees, rather than the new investors. *(Analogy: It is akin to a homebuyer demanding the seller build a new garage out of their own pocket before finalizing the agreed-upon purchase price, ensuring the buyer gets the upgrade without paying for it.)*

*   **Setup:** A term sheet will stipulate a target post-money option pool—frequently 10% to 20% of the fully diluted equity. 
*   **Mechanic:** To achieve a 15% post-money option pool, the founders must issue the necessary shares out of their pre-money capitalization. If a company with a $10 million pre-money valuation raises $2.5 million, the post-money valuation is $12.5 million. The investor buys 20% of the company. If the option pool must be 15% of the $12.5 million post-money, the shares to fund that 15% are subtracted from the founder's pre-money equity value, effectively lowering the actual "effective" pre-money valuation [cite: 6].
*   **Synthesis:** The Option Pool Shuffle underscores a critical reality of venture finance: the headline pre-money valuation is often an illusion. By forcing the option pool into the pre-money capitalization, investors mathematically reduce the price per share they pay, ensuring they absorb zero immediate dilution for future hires. Founders must rigorously calculate the exact size of the option pool needed for the specific operational runway between financing rounds to avoid unnecessarily stripping their own equity.

### Pre-Money vs. Post-Money Valuation Paradigms

The valuation of a startup is bifurcated into two distinct phases: before the capital is injected, and after. 

The **Pre-Money Valuation** is the agreed-upon value of the startup's existing operations, intellectual property, team, and market traction immediately prior to the new investment. The **Post-Money Valuation** is simply the pre-money valuation plus the total amount of new capital raised in the financing round. 

While the arithmetic is simple, the distinction dictates the price per share. The price per share is always calculated by dividing the pre-money valuation by the pre-money fully diluted shares outstanding (including the expanded option pool, as noted above). This mathematical relationship ensures that the incoming capital explicitly purchases a specific percentage of the post-money entity. 

### Early-Stage Instruments: SAFEs and Convertible Notes

In the nascent stages of a startup, establishing a precise pre-money valuation is often an exercise in fiction, as the company may lack revenue, a complete product, or clear market traction. To bridge this gap, early-stage finance relies on convertible securities—instruments that inject cash immediately but delay the valuation exercise until a subsequent "priced round."

Historically, the dominant instrument was the **Convertible Note**, a short-term debt instrument that converts into equity. Because it is legally classified as debt, a convertible note carries two distinct hallmarks: an interest rate (typically 2% to 8%) and a maturity date (a deadline by which the company must either repay the principal plus interest or convert the debt into equity) [cite: 10, 11, 12]. If no priced round occurs by the maturity date, the startup theoretically defaults, giving the noteholders severe repayment leverage, which can force the company into bankruptcy or compel founders to renegotiate punitive extensions [cite: 12]. Furthermore, the interest on the note compounds over time, meaning the accrued interest converts into additional shares upon the eventual priced round, directly increasing founder dilution [cite: 6, 12].

To eliminate the complexity, legal costs, and existential risk of debt maturity dates, Carolynn Levy at the startup accelerator Y Combinator introduced the **Simple Agreement for Future Equity (SAFE)** in late 2013 [cite: 13]. The SAFE is fundamentally not a debt instrument; it functions more like a warrant, accruing no interest and carrying no maturity date [cite: 10, 12, 13]. It allows a company to raise capital rapidly, with the investor's cash converting into equity upon a future triggering event—usually the company's first formal priced equity financing [cite: 14, 15]. 

To compensate early investors for the extreme risk of backing an unpriced startup, SAFEs and convertible notes utilize distinct economic incentives:

*   **Valuation Caps:** A valuation cap establishes a maximum "ceiling" valuation at which the early investor's money will convert into equity, regardless of how high the valuation is in the subsequent priced round [cite: 10, 16, 17]. If a SAFE holds a $10 million cap and the subsequent Series A is priced at a $20 million pre-money valuation, the SAFE investor converts their capital into shares as if the company were only worth $10 million, effectively yielding shares at a 50% discount.
*   **Discount Rates:** Alternatively, or in conjunction with a cap, an instrument may feature a discount rate. A 20% discount rate stipulates that the SAFE investor will purchase shares at 80% of the price per share paid by the new institutional investors in the priced round [cite: 12, 16].
*   **Most Favored Nation (MFN):** An "Uncapped MFN" SAFE contains neither a valuation cap nor a discount. Instead, the MFN clause guarantees that if the startup subsequently issues a SAFE to another investor with more favorable terms (e.g., adding a valuation cap), those better terms will automatically apply retroactively to the MFN SAFE [cite: 12, 18, 19].

**The 2018 Post-Money SAFE Evolution**

A critical shift in startup fundraising occurred in 2018 when Y Combinator updated its standard template from a "pre-money" SAFE to a "post-money" SAFE [cite: 10, 17, 18]. 

Under the original pre-money SAFE, the valuation cap applied to the company's valuation *before* any of the SAFE money was converted, meaning founders and early investors could not calculate their exact dilution until the subsequent priced round occurred, leading to cascading, unexpected dilution when multiple SAFE rounds stacked up [cite: 6, 13, 17]. The 2018 post-money SAFE fundamentally altered this dynamic. By measuring the safe holder's ownership *after* all SAFE capital is accounted for, but *before* the new priced-round capital is injected, founders and investors can immediately and precisely calculate the exact percentage of the company sold [cite: 12, 18, 19]. If a founder raises $2 million on a $10 million post-money SAFE cap, they know definitively that they have sold exactly 20% of the company, regardless of when the next priced round happens.

**The Interaction of Multiple SAFEs**

A critical consideration for founders in 2026 is how multiple SAFEs interact before a priced round. Unlike convertible notes, which convert sequentially and can dilute earlier noteholders, all outstanding post-money SAFEs convert simultaneously at the exact same moment during the priced equity financing [cite: 12, 19]. Because each post-money SAFE locks in a fixed ownership percentage of the company at signing, they do not dilute each other; instead, their combined dilution "stacks" entirely onto the founders and existing common shareholders [cite: 17, 19]. To maintain a clean capitalization table, founders must aggressively model their fully diluted conversion across all SAFEs, factoring in option pools and aggregation before the priced round closes [cite: 6, 12].

#### Table 1: SAFEs vs. Convertible Notes

| Feature | SAFE (Post-Money Standard) | Convertible Note |
| :--- | :--- | :--- |
| **Legal Classification** | Future Equity Contract | Debt Instrument |
| **Maturity Date** | None | Fixed (e.g., 18-24 months) |
| **Interest Rate** | None | Yes (Compounds and converts to equity) |
| **Dilution Dynamics** | Fixed percentage at signing (stacking directly onto founders) | Variable, sequential conversion |

### Priced Rounds and the NVCA Term Sheet

When a startup matures sufficiently to attract institutional venture capital—typically at the Series A stage, where median pre-money valuations reached a record high of $49.3 million in Q3 2025 [cite: 20]—it executes a "priced round." During this event, a lead investor assigns a hard pre-money valuation and purchases newly minted Preferred Stock.

In the United States, priced rounds are overwhelmingly structured using the model legal documents published by the **National Venture Capital Association (NVCA)**. Since their inception in 2003, these documents have become the industry gold standard, democratizing access to top-tier legal structuring, drastically reducing transaction times, and eliminating traps for unenforceable provisions [cite: 21, 22, 23]. While priced rounds entail significant legal costs and friction—often tens of thousands of dollars in legal fees and months of negotiation—using NVCA templates drastically mitigates this friction compared to bespoke legal frameworks, whereas SAFEs are designed to be executed swiftly and cheaply using standard, unmodified templates [cite: 17, 23].

The NVCA suite comprises five primary documents, which act as a heavily interlinked legal apparatus:

1.  **The Term Sheet:** The foundational, predominantly non-binding blueprint that outlines the economic and control terms of the investment [cite: 23, 24, 25]. It serves as a roadmap for drafting the definitive agreements [cite: 26].
2.  **Stock Purchase Agreement (SPA):** The binding contract formalizing the sale of shares, containing exhaustive representations and warranties about the company's operational, legal, and financial status [cite: 22, 25, 27].
3.  **Investors' Rights Agreement (IRA):** Governs the ongoing, post-investment rights of the investors, including information rights, registration rights, and rights to future issuances (pro-rata rights) [cite: 21, 25, 28].
4.  **Voting Agreement:** Dictates corporate governance, specifically establishing the composition of the board of directors and enforcing "drag-along" rights, which compel minority shareholders to vote in favor of a company sale if approved by a stipulated majority [cite: 24, 25, 28].
5.  **Right of First Refusal and Co-Sale Agreement (ROFR/Co-Sale):** Prevents founders from secretly selling their shares to third parties. It grants the company and investors the right to buy the shares first (ROFR) or participate in the sale on a pro-rata basis (Co-Sale) [cite: 22, 25, 28].

**The October 2025 NVCA Updates**

The NVCA documents are not static; they are updated to reflect shifting macroeconomic and regulatory realities. In October 2025, the NVCA released highly significant updates driven by heightened national security concerns and operational efficiency trends [cite: 27, 29].

The most critical recent change was the integration of compliance mechanisms for the **Outbound Investment Security Program (OISP)** and related bulk data regulations [cite: 22, 27, 29]. The updated Stock Purchase Agreement now mandates strict "two-way" representations and warranties wherein startups must confirm they are not engaged in any "covered activity" under the OISP, have no intention of becoming a "person of a country of concern," and have no direct or indirect ties to "covered foreign persons" [cite: 29, 30]. For practitioners, this necessitates rigorous diligence checklist refreshes, including data-flow diagrams and compute location verifications, significantly raising the compliance burden for SaaS and AI startups [cite: 29]. Furthermore, the October 2025 update formalized mechanics for *tranched financings*, streamlining venture deals where capital is released sequentially based on the achievement of specific time- or milestone-based performance targets [cite: 22, 27, 29].

### Structuring Downside Protection: Liquidation Preferences and Anti-Dilution

As highlighted by Kaplan and Strömberg's application of financial contracting theory, venture capitalists require distinct control and cash flow mechanisms to protect their principal in downside scenarios [cite: 1, 3, 4]. The two most potent economic levers in a term sheet are liquidation preferences and anti-dilution provisions.

**Liquidation Preferences**

A liquidation preference determines who gets paid first—and how much—in a liquidity event, such as a sale of the company or a dissolution. It is the defining feature of Preferred Stock over Common Stock. The preference is expressed as a multiple of the original investment (e.g., 1x, 2x) and falls into two distinct operational categories. *(Analogy: A liquidation preference acts as a debt-like shield that ensures investors take their money off the table first during a corporate 'fire sale' or exit, before the remaining equity pie is sliced for the founders and employees.)*

*   **Non-Participating Preferred Stock:** This is the accepted market standard in the U.S. venture ecosystem [cite: 31]. Upon an exit, an investor with a 1x non-participating preference must make a mathematical choice: they can either take their guaranteed return (1x their initial investment) *or* convert their preferred shares into common stock and participate pro-rata in the proceeds based on their percentage ownership [cite: 31]. They will rationally choose whichever option yields a higher dollar return. This structure protects the downside but prevents "double-dipping" in high-value exits.
*   **Participating Preferred Stock:** Widely considered a founder-unfriendly, aggressive term, participating preferred allows the investor to "double-dip" [cite: 31]. The investor first takes their 1x preference off the top of the exit proceeds, and *then* participates pro-rata with the common stockholders in the distribution of the remaining proceeds. 

#### Table 2: Participating vs. Non-Participating Preferred Stock

| Feature | Non-Participating Preferred | Participating Preferred |
| :--- | :--- | :--- |
| **Primary Mechanic** | Investor chooses: 1x Preference OR Pro-rata conversion | Investor receives: 1x Preference AND Pro-rata conversion |
| **Market Standard (2026)** | Dominant / Founder-Friendly | Rare / Highly Aggressive |
| **Exit Dynamics** | Prevents "double-dipping" | Enables "double-dipping" |

**Anti-Dilution Provisions**

Anti-dilution clauses protect venture investors if the startup subsequently issues shares at a price lower than what the current investors paid—an event known as a "down round." By adjusting the conversion ratio of Preferred to Common Stock, the mechanism retroactively lowers the price the previous investors effectively paid.

There are two primary methods of calculating this adjustment. The **Full Ratchet** is the most punitive to founders: if a single share is issued at a lower price, the original investor's entire block of shares is repriced to that new, lowest price, regardless of how many new shares were issued [cite: 15]. Because this can obliterate founder ownership, the market standard is the **Broad-Based Weighted Average** method. This formula adjusts the conversion price based not only on the lower price of the new shares but also on the *volume* of shares issued relative to the fully diluted capitalization of the company. 

The Broad-Based Weighted Average method provides a tempered, proportional protection. This mechanism became intensely relevant during the tech market correction of 2023-2024, where a wave of 'down rounds' triggered these clauses. By late 2025, the rate of down rounds had stabilized to roughly 17% of all new venture rounds, down from highs exceeding 20%, illustrating the real-world application of these anti-dilution protections in resetting valuations while preserving some founder equity [cite: 20].

#### Table 3: Anti-Dilution Mechanisms

| Feature | Broad-Based Weighted Average | Full Ratchet |
| :--- | :--- | :--- |
| **Repricing Formula** | Factors in both the new lower price and the *volume* of new shares issued | Automatically reprices to the lowest share price regardless of volume |
| **Founder Impact** | Tempered, proportional dilution | Extreme, highly punitive dilution |
| **Market Prevalence** | Universal Industry Standard | Extreme edge-case / Distress financing |

### Operational Runway and Investor Metrics (Current State: 2026)

Runway is the number of months a startup can operate before its cash reserves are depleted, assuming current revenue and expense trajectories remain static. To secure funding in 2026, founders must align their runway and operational performance with stringent new benchmarks. The macroeconomic shift away from the speculative fervor of 2021 has resulted in a landscape where efficiency metrics are viewed with the same scrutiny previously reserved solely for top-line growth [cite: 32, 33]. 

Secondary market aggregators and investment banks—such as SaaS Capital, Bessemer Venture Partners, Software Equity Group, and Carta—track these benchmarks, establishing the threshold for successful capital raises. Notably, the median wait time between funding rounds extended significantly to 696 days by Q2 2025, mandating that founders plan for significantly longer capital efficiency periods [cite: 34].

**1. The Burn Multiple**

The Burn Multiple, popularized by venture capitalist David Sacks, has emerged as the definitive screening metric for capital efficiency in 2026 [cite: 32]. It measures exactly how much cash a startup incinerates to generate a single dollar of Net New Annual Recurring Revenue (ARR). 

A Burn Multiple above 2.0x indicates that a company is spending more than two dollars to acquire one dollar of new ARR, a highly scrutinized red flag in growth-stage companies [cite: 35, 36]. In the 2026 market environment, companies presenting a Burn Multiple above 2.0x face severe penalties, often experiencing a 30% to 50% valuation haircut compared to efficient peers, or outright failure-to-fund, as investors decline to underwrite systemic cash inefficiency. The 2026 benchmark data establishes that a Burn Multiple below 1.0x is considered excellent, signaling that growth is nearly self-funding [cite: 35]. By stage, median Burn Multiples in 2026 sit at roughly 1.6x for Series A, tightening to 1.4x for growth-stage companies ($25M+ ARR), with elite AI-native SaaS companies consistently outperforming at 0.8x to 1.2x [cite: 33, 36, 37].

**2. Net Revenue Retention (NRR)**

NRR measures the percentage of recurring revenue retained from existing customers over a specific period, accounting for upgrades, cross-sells (expansion), downgrades (contraction), and cancellations (churn) [cite: 35, 38]. Because acquiring a new customer is significantly more expensive than retaining an existing one, NRR has become the "north star metric" for sustainable enterprise software companies [cite: 32].

An NRR above 100% indicates that a company's revenue will grow organically even if it acquires zero new logos. According to 2026 private market benchmarks, the median NRR for B2B SaaS is hovering around 106% [cite: 38, 39]. However, "best-in-class" companies command an NRR of 120% to 130%, a threshold that nearly doubles a startup's valuation multiple in M&A scenarios [cite: 38, 40, 41]. Elite performers achieve this through embedded product stickiness and deliberate expansion strategies rather than one-off upsells [cite: 36].

**3. ARR Multiples and The Rule of 40**

Startup valuations are fundamentally priced as a multiple of Annual Recurring Revenue. Following the market correction that compressed peak 2021 multiples (which frequently exceeded 20x ARR), the 2026 landscape has stabilized into a "new normal." 

Current data from SaaS Capital (2025/2026) indicates that the median private SaaS valuation sits at 4.8x ARR for bootstrapped companies and 5.3x ARR for equity-backed companies [cite: 40, 42]. Public market comparables trade slightly higher, with the median public SaaS company trading around 6.4x to 7.0x ARR [cite: 41, 43]. However, there is a massive bifurcation based on performance and sector. Companies exhibiting AI integration command premiums 25% to 50% higher than non-AI peers at every funding stage [cite: 37]. 

The primary determinant of whether a startup commands the 5.0x median or a 10.0x premium is the **Rule of 40**. A synthesis metric favored by late-stage investors and acquirers, the Rule of 40 dictates that a healthy software company's year-over-year revenue growth rate plus its free cash flow (or EBITDA—Earnings Before Interest, Taxes, Depreciation, and Amortization) margin should equal or exceed 40% [cite: 32, 35, 41]. In 2026, companies scoring above 60% on this metric frequently see valuations 2 to 3 times higher than peers scoring below 20%, proving that buyers reward the deliberate, disciplined balance of growth and profitability [cite: 39].

### Future Outlook: Venture Structuring Post-2026
Looking beyond the immediate 2026 landscape, venture finance is shifting toward more structured liquidity and concentrated capital deployment. With a persistently challenging environment for Initial Public Offerings (IPOs), late-stage startups are increasingly reliant on "bridge funding" and secondary market liquidity to retain talent. Tender offers are on a dramatic rise, with companies conducting nearly 400 tender offerings on the Carta platform in 2025 alone (a 62% increase from the prior year) [cite: 44]. Furthermore, the overwhelming gravitation of capital toward capital-intensive artificial intelligence (AI) startups—which absorbed 58% of all Series D cash in 2025—is bifurcating the market [cite: 44]. Standard NVCA documents will likely see continued evolution to manage the unique hardware and data security constraints of AI-native companies, cementing a market where "standard terms" are rigorously gatekept by regulatory compliance [cite: 27, 29].

---

## 2. Formulas & Quantitative Relationships

Venture finance relies heavily on precise mathematical relationships to structure term sheets and evaluate operational health. Below are the definitive formulas utilized by venture practitioners, investment bankers, and startup operators as of 2026.

### Core Valuation and Dilution Formulas

**Post-Money Valuation**
The foundational relationship in priced equity rounds, dictating the total enterprise value immediately following the injection of new capital.
$$PostMoney\ Valuation = PreMoney\ Valuation + Total\ Investment\ Amount$$

**Price Per Share (PPS)**
The price an incoming investor pays for a single share of Preferred Stock. Crucially, the denominator must include all outstanding shares, options, warrants, and the unissued options explicitly designated in the pre-money option pool expansion.
$$Price\ Per\ Share = \frac{PreMoney\ Valuation}{Fully\ Diluted\ Shares\ Outstanding\ (PreMoney)}$$

**Investor Ownership Percentage**
The raw equity stake purchased by the new investor.
$$Ownership\ \% = \frac{Total\ Investment\ Amount}{PostMoney\ Valuation}$$

### Capital Efficiency and Growth Formulas

**The Burn Multiple**
The 2026 standard for evaluating capital efficiency, measuring the cost of growth. "Net Cash Burn" is total cash expenditure minus total cash revenue over a given period (usually quarterly or annualized). "Net New ARR" is the total new recurring revenue added in that same period.
$$Burn\ Multiple = \frac{Net\ Cash\ Burn}{Net\ New\ ARR}$$

**Net Revenue Retention (NRR)**
The ultimate measure of product stickiness and account expansion. Calculated over a rolling 12-month period, it measures the revenue retained from a specific cohort of customers.
$$NRR = \frac{Starting\ ARR + Expansion\ ARR - Contraction\ ARR - Churn\ ARR}{Starting\ ARR} \times 100$$

**Gross Revenue Retention (GRR)**
Unlike NRR, GRR isolates a company's ability to retain revenue strictly by avoiding churn and downgrades, stripping out the benefit of expansion or upsells. It is mathematically capped at 100%. Elite 2026 SaaS companies maintain GRR above 95% [cite: 39].
$$GRR = \frac{Starting\ ARR - Contraction\ ARR - Churn\ ARR}{Starting\ ARR} \times 100$$

**Customer Acquisition Cost (CAC) Payback Period**
Expressed in months, this evaluates how quickly the gross margin from a newly acquired customer repays the sales and marketing costs spent to acquire them. In 2026, a median benchmark is 15 to 18 months, with elite companies aiming for under 12 months [cite: 39].
$$CAC\ Payback\ (Months) = \frac{Customer\ Acquisition\ Cost}{New\ Monthly\ Recurring\ Revenue\ (MRR) \times Gross\ Margin\ \%}$$

**The Rule of 40**
The premier valuation lever for growth-stage and scaled software businesses. It quantifies the trade-off between top-line expansion and bottom-line efficiency. (EBITDA equals Earnings Before Interest, Taxes, Depreciation, and Amortization).
$$Rule\ of\ 40\ Score = YoY\ Revenue\ Growth\ Rate\ (\%) + EBITDA\ Margin\ (\%)$$

---

## 5. Gaps & Caveats

While the legal parameters of venture capital—such as the October 2025 NVCA model document updates and the YC Post-Money SAFE definitions—are rigorously verifiable through official primary source documentation, a rigorous practitioner must acknowledge the inherent limitations surrounding the quantitative metrics presented in the current market.

1.  **Opaqueness of Private Market Multiples:** Real-time data concerning private SaaS Annual Recurring Revenue (ARR) multiples, median round sizes, and Rule of 40 valuation impacts rely exclusively on secondary data aggregators, consultancies, and brokers (e.g., SaaS Capital, Bessemer Venture Partners, Software Equity Group, and Carta). Unlike publicly traded equities subjected to SEC-mandated audit standards, private startup transaction data is voluntarily self-reported or extrapolated from proprietary platform subsets [cite: 37, 40]. The cited medians—such as the 4.8x ARR for bootstrapped companies and 5.3x ARR for equity-backed companies in early 2026—should be viewed as highly informed directional benchmarks rather than universal economic laws [cite: 40, 42].
2.  **The "AI Premium" Volatility:** Throughout 2025 and into mid-2026, market data consistently demonstrated that AI-native or AI-integrated SaaS companies command a 25% to 50% valuation premium over non-AI counterparts across Series A, B, and C rounds [cite: 37, 44]. However, as noted by industry analysts, the market currently struggles to distinguish sustainable AI integration from superficial positioning. The ARRG Multiple (Price-to-Earnings growth equivalent for SaaS) indicates high volatility; therefore, the stated AI valuation premiums are highly fluid and subject to sudden recalibration depending on regulatory shifts and technological commoditization [cite: 45].
3.  **Deviation from Standardized Models:** While this brief outlines the canonical forms of early-stage (SAFE) and priced round (NVCA Term Sheet) financing, practical reality frequently diverges. High-leverage founders routinely negotiate custom side letters altering pro-rata rights, and dominant lead investors frequently push for participating liquidation preferences during economic downturns despite the 1x non-participating structure remaining the quoted "market standard." The actual allocation of control rights—as theorized by Kaplan and Strömberg—is ultimately a product of bespoke negotiation rather than rigid adherence to a template.

**Sources:**
1. [oup.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHy2BV-gRQfqD0lGRiJusa_mlx9yp_9QRU7toWB5U-kJYXEcCjlH0VSZYsS_xRBB1kX9bcOmNWQBj10n0_cG_y1XjOX5tRm9Ut41jggTDEai_FmZvrYUcSFNwigVAk_oz5SSwXrv_wU3hqg3rCQ_JFKqZGdkY6U)
2. [liuyanecon.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHOdNpy5FAEI5eIXs-9q6mjyGqOylhS39qUSRRvRa4dRBzdhMS5fzGdLv6vDfuMtHdlQj9TF3jcs1GKObaDfGbJbCN5VtNRTQxdB2Pl61oWCBJylCpsYdfiZtNz9a-SYNiKJVXJZtKQheCs_xTfHI1peFVKbrjl9hA=)
3. [google.se](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGlY9eeufEuQBOPo59Q6PwfcVkOFwv60tXZQzr9hEukUeQw3jWjmkJyJh8NXfhymyHyydDTmQS7GfMleeGcSL2IdTEujNa3UqyGk_CGJnH_hYKVAVdu11lTylPW9xvkS810InH1Z6RM47tm8dPULBtQ)
4. [edegan.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKyfm0bdL625fhGJ5msVhFO22WlAQBaQdACThztq_PRpavZRV-DN1_us4wCjs9r66thVHNg2ylLrlYOACorvYYx1W22yRPEhzxMOGPDS2_ur8cw4lp8H7eu7KOsb77wcIBOr2l66t4OOsiHv6UNOA7zbHGStaFrK_S2ABVxaviiMgHIg==)
5. [carta.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGoCOVBDU934RkBCrvkLKuOaw2YJ4Ex7RyMpinS-W_MU2FFWmVQjncS9KYoz3x_zjJs3EdVKKeWH40v4AJj6YgSX4lAPawncBV7GSFe6htfCJvCi6QtuWgy8iCXuStuGA==)
6. [glencoyne.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtOBujnnTN43RGLwUWu-fk2uCD10uJadMOgDySxcTSXP2yyi6OhPJF4iMB8lKu9y2KkS0hJh_tgkgB0EzLlBBUuu6VSceW34Xp1-zOIluQqaPC0y3LLC3OP2f18rNCzC9Mt0rA8LHkhW7lCAda-vvNAY9Ijw==)
7. [alibris.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEz-lNR6uQMijWDr8fzGlKc9VjCDSe3wsYh_71S8hinCHk__a3H2r2AcemSjBDrm8bHFnZWV2tpseTYVRWeP2xWgACN45TuDhH5I6lUQ1t1tvKR75HPWO9g0n5wY2pfbmQtto25ZZf6nAAEjhMNXD8zAlTXD28u)
8. [abebooks.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHkfxvjzJYzfKtLLf3BIk9Iy45EPKfYiu2U84uPsn_24m5-vSm9vzfEc15vkLIVIVA_11iy5vI6f36goE86CTTgKJzQcXYeGwBlIRVt9HaQkCSF990jgHLxNvqiZgHxoZWn981uZfvZ4UGEFJd9bhNWU5merB52DjVecCtbPsz4L3yfFKLnBLMPXxkR67KkWL-BJA==)
9. [porchlightbooks.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF6y57qNbDYpdHS5LLijUyLxienqdufLqzlxrXjnJY-Uoow32v4J98-3xYT3UjW6n9W7o1Hvf8G-BuqiXlvkkPv9MIDHadswz2ePhRHpELV5FLoxU9QXebzinmx-mPX-STXlXj6rZtXWetka61_irREynOMyACM_ItmbOwtRGp60bVwGg==)
10. [thomsonreuters.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFJAbgRMDw5Of2GLoUoV2KnpY_ln88f2xMdaG3AsOl96ZSkDAszQUV12s5HKEifTMnjXOcvVviVfZ1QFd8HWaPZ5IwrufLjOOdrqbIgHMXqqOiADMT1G3kvbDV544CBBJM_fW9FA55cz-U-NVm6GXTHjiOkpGeXe-3w2sISuDln6EE-Sl6hSdi52iKLUPxuWIhKBB7Kowvv)
11. [fe.training](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHLeiuYJWdT2TTCUyOQFQzRFkrCK_umuCPf5YhgWoB-OEYvjdfxMbCSXG4ewkXMYsMYRl6F3ZAkRsQ4r3cU7BZ_f0Tt66a6svh3ZUyb_yziiOrPZ1hH5tPw-z0fR7VIVLzAjmq3F-ZszvgMsGsrI6JLQ51OVmpkqvOYTWVRmsr9aWdtVuJzzstYfK1wlCf0qhCWB1jR)
12. [promise.legal](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHYN37n1QMjLbnDXOzmpKZBcSlO2XDL7wBmeR8xGhW295Alhq9PxMinMoS0s24UQ0etpxDfXAJchmttohJOOm929x-U93l7eZMjGepSZXUklJsggXPdjRnRloR-sP4P6lwfc5Kb_a6QUf8mlxOF_WHbFgN6Ht60P0j_hPIzJbcUyqIetJn7hXnp6WIgPnRY8cpjaMq66Eq05K0MGwSBRi3aPb3O_OMUSKRKaikJ_4OojD61)
13. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQExFSPdu5oeVOO1RuhN9gMbpA429c9xs7sEclCtsOZbPxH5ziVKqlPZ095QxhB5BZohmnvs_NkgDj3Qf41AF2Y7Jt1owl7aAZ1HnNqMcLWTESJJ72aYzpdf8mT1CeglIrwxr_i2A-VJHVcV7YxhKsYaMWoZFvE=)
14. [carta.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxtDdylxAiJ88-B-tGbFL0JVBViL1vpLbotA1bv9_YCf-809_rXc4n01yErEtIxsRfrnGXnjXbOUuH9e49GLSoPYNyRj0iiQ3lvq8SWBV2ooKYyz53QsIsSvZ_3Lqq-oraFy42SSBWckD9VRIYvQTrwViCaq2DtOzLYxTkbr_M)
15. [eisaiah.blog](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEoaP5Rt7xi8aQlmYXyafS1qi1TCcXpOxC4CrtbbtNeMZut-Y82zPrwbW-V6lgIAoMI0JcIwPuncVgFma61Pey51japJLMgBCEJr-IJAlOUW4kEEtqZEBl8SIv6apQVufy-ThYLJf4lXoP-lKweJiUbKmI=)
16. [wallstreetprep.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHxZxeYCEURrdOTx0VQ2d6aP8jSRgvM4RpuNvHx1nMQtnL-2xrNPVaKunv_bQXUksts-3N4SlXJc_9cFgilcPfThoUuaP5Wf-LQbFII94DOJrEd22uzJuUHwjPtU6hPMq5wfDZFDNceGQ==)
17. [crv.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEwIiVYAeI6nfS5D7n6R_H_oRMTqcv8O7z88LMsP3hOT7x5lkE9ABjiwBI5wKyHSwjLye-m4ogjb-zIxyBYIg04XK3HLJu4ohFfNilNQC3VUtO4sRFknKjbTF_Kyhe-hMDWWRui8er92LyFJ-Z8)
18. [ycombinator.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFkApoTKP7BVk5QiTYkm9U1RCwShIdt06DzklM88pSkoDpjFDBVznxU3JOO5FXyEEOMnalEf6tHR_dTD6OQpJIMYAHAkLDAZRiAV-K4Mb8wle235FoR5JlH0-8=)
19. [capytable.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG9nsKBEsR6HFy_KsVXuCz_jqtrRrdFHZ8EYrd3qGBHVD04uElJW80MIOizfi-nKaCPYp05cMStfYIN_pHG2NeWSwG_JIcL_FUh7KFsN8VfHO8XK5I0YJrufiULK8Y1-AeGXg==)
20. [carta.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFtxvZPufCTLJFs3vyXkmd89UkkiI5hqNmZDLqNoB8rmrklwSM-n4E0UTkPT9YaAokJumsigX2Kd-RyW_-z0Zq1soq3W3s_BVm564zdJx78F9_C7LP8Gs28_Lavt-CnuEP7fbEiP2BDRG2F2ucC)
21. [paulhastings.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH_0BJwkiDsEYQcgE8NwqKX1xLetQT6R2DaWoO8foTcXPkhYVavo7gDRgnVRAZstDj3sRSLTm_5uy1FD06kZirowcmpHW-KV5HxqEPK4VGB5NEahTxvJgIuX87rFfbLNfhTQmGu6b0BI9dxSkDaUo86eqTLHnJv9-4Lzaga4MJx49MGs7mHq_2fZ9T3LKc5WEAKUx2BcSjI1_U7QJrsXzfY6Fz8)
22. [nvca.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEKzEioOtdLKqjFrmMPKblDy91I_L5Dgo4E80eKVfcM66tDks__Z7-dyzo3IDo0mgq65-bLDBz6kuIV27HwljOeOT08tQYjqamx4h45QxFUwpcujQmiziyXdCF-8Q==)
23. [venturecapitalarchive.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF7-5f9Dpn-t-oCgeAS9coE_w6s9Awv-faABsxpD7HUfL5ZGo7e-20Y3hQEuuwfhPCqqA-QIK8izxmHh9ImJsGUStILiHUHr7xMGpqysA_BlXLalzOzJcHi45m9AYW75BDFtF9EqEE-cGF0IwA_hVFaRlO5M4AttbnAmJLbyKE=)
24. [eqvista.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHEgjI94SpvWYYJMplc_Y8cz4v-aRhvnfM4Atni6CI_YzgwvF_5lCO6DEn2ye-GhtCf4RuGcLPan7yZ_TWZbT-wnXCQjmMMDrcX2StyG-b26ogcibXU1UHm36VY3x6fx7TtVlY=)
25. [fourscorelaw.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFk1rf37X3PrJ6n2RXKVC05HijdXGtxt_wVg-OKrLSiRaicOYQ_XcwyAnPfqCUpJLTF6ikPLfYRY00VODb0T9clzA0168Of17y1XOOYHzhi_uDRV40dp-lRkVmqkH3uFiys_BCPGxLkvbGybZOKtxny2LrVYvqL9S8U0_S1mPXPR8Xfxzp2zHLwYtbaEqBpzf6Hh1egxpOUESU2VSCvEboqJDYb)
26. [nvca.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvZEM90JoHZA2CLcdl5k2XCybgkyCZq5c8KjJqpfc33emnqsJr6JpNRpHPEpBeN38Z1mOYBAu6Db-rEF1Nu5XEdtnXy7SqJGaIVDndpBqSgCIOGRhGurxn4tD12gwFudMvM2t9sVSgxdEZsIjw-RH08ZDlOWip9tIDydll)
27. [nvca.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFh5ulmbmJwcwIyv7ziosMDWJ2rbvyyUY4gB35PaaO6hRPaa05Nb0FpGR_j3I0RrF-ikBR-ZKlAjgb6ixSlas9Vca5Xl2Ppr10j8rgjlaaY0A0QRiHlSmYDfZ-gLrAFPc7QwDyQxZ6GQuwKvpjw3crjztU7mbN4aSL0J7S66ombdfFgMh2zfWUUtQ==)
28. [nvca.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHa0f_b3NNrt19hsuJr6FsPebxnul2-axiCirphZk89mWIFBhVmWICK1ZYED1gvDTiY_eu_kfkc6srs0jvQMOiKeW6SUCGb1bLO0V9Q7vvCcxoJwqVLAwAoIXnzichSO22PlmPcC1mgOSm-iSJovA==)
29. [foley.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEM4kyfkCLGk2hyTG6yEElhlCqzfaaLsPrfdiFJINLmn8KPD6nx2KXkv7SbwgrwtTyXkDvmPMNv6wV4onV53hid__VXCjwMHUfw9vtuTcSuFM33LVoElgQeVIfNBq4hfQsBa-GpQRvQ1nUDlrB43AFTRrRdmAUT0I8Ob78s1SOqUpOnFhDMRAM84chOtb0_AF3r-9G8_9g_GPQiTl7x40NNLLXc)
30. [nvca.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHuXMr5kJCr9E3pES3fHa1zdajDcYsIKN57fDH_aoS2hIvlzXND4S6oQbEQ-KVoB9PXm_pVmG68WeuQft1fxVV-g8oJfNX1R7U7V2haJlcNWZFs26cK-l82k3LVv7VymXanFr6wZpZNke0slgQBCt1eGKGNJgsTjKtJkUuy6OdUtYouBM_4i62vfFwfTfxghhA5Ny-lsksHOSoUvgNUZZA=)
31. [glencoyne.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFKhIFdsjfKzTGYK3p7F5isz1jPjaySa_8KcZ4TLtvbApL78MfyfDD20gPQYzLS9oGQFWkZNwawKkddlQ_XMuXFCSFLMNAaUNi0saDvLXDdC51ANhSxZbJiPt71s1dDIU6rIOMQHvKelYtvLfYZ6uzhKnI=)
32. [substack.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEkplL7ddOOtY_SrF023yCMZ0jG_tfjlN3xcGBZSVXCwEUHzXLVm7jEAUuEITIfwFoq8azOBaqJ2hE9a8goQSKcWhh7zKpFCK8aoZf0l_ULO4QTKYwpJh17asoZ84Siiyzu7BN0gQ43cGjiHnhYQVhP)
33. [saasmag.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHon9CIYjSh2lDeRBneDzRl7auCccEM2DYPvEGOeqy4izMrc9dQO98Gbq7OfD3KhwlyynyEiHUqnzl7jTKpC1xnLh8hEaKXyID_CJyW-_k67eYNcbB4Xs1THqHyzAVgTE_hHYTGT5pURIUvVlYG)
34. [carta.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE9l4Nu4__qEvmnCdwWe6sTcoPn5uM8yDS2e3azDtQLhR1r2A2pTdTtGQz9veTTeGtQ135szvhFD9PJayxALRJuWCbzx5djBd8ZJ_Naj2iWQb0Y7MYG-qOaUB1AUhrslxgjcN_SOpLLqNjhaRq1)
35. [designrevision.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEmmPU-GtbfnpNxJasSOHVPkYQ11fvAF9xEjrMSHcSA5wv_wWI2Jx1ypuiUuq_JV-_69A8nwGO_rb6I-tDjdUkeMn5OwMCjhRZwuKhRji7BUcv-PNZwIZRwXXs24eos76cK6f2jVEafyiL7FA==)
36. [data-mania.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGpZrX1-oeTkpxM6foqAZK8Zma9HGZIJCa0PAOm_xZ6nn2huqiMFqk9R4iboto-wbPBJkCziyDAWDyhd7eoH9XxtBuNHrXAQGObeIorr3egNazJhLHszDWBkVnKRLNZ67X2B2bqXOfk6bHPmo2lknZfx4Sbr4LYNGlJZDpOcY1Xh5sQ7M8TXbEfttFfZ1Iq_RZ9BcPhZrLoPwEv360-dZNjgR6pAYGe)
37. [saasvaluationmultiple.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGVyfCF_j7E7g6GVyvrvPcwGGjHes11DMDeOLn1rd3-Y5TMm96fwa0m-7kMvsSER7Cncx6t0lInNmuEmqvi-e5-XilUuIUx9t33hcOJPQ3OlafquE02an7bZ5Gpd6UvJg==)
38. [averi.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGkeigqJRxIMw_L9mjkOA4_Z5gA01v4krwgCwl-BTw8vr2udPxoVwishVrxePqVKomFhwOhCV0P9F0ryNfCnn_LB-70OO5QW0bwMkJKvhc5sv0ShUSAxtnKP_KvqoAHtbdag2zeaQxwuLJqfN9rm9QgWvS5oKmy6D4MsND491igNNinTAwWciKJ10rAboMHeJE1COa3QIKAemZrUw==)
39. [phoenixstrategy.group](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFS2e6MfHgfMcvhPZY__6g19YFekPFXxy18fH0JA5L80GoGAES0aA5G4SgLJ6DUO5kh7qoYxGfsDzceHpKGB6QAZIY4lVgiT5ZiD1tIFIuy06ilkoxwyz-6a3ozeKEcg43eTMnfBmOaWGeGF479NxUKZoDD2b2MNfoOXaseZDwDKRDpmnsmS4HtM3M=)
40. [startupa.ge](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHfwbEVkfOiqUdWKHST3iByrdGaF8z4uJHa3XspsSzplPgyea5WJrdvKftV1RdAONtKiSX1U_xEBRmdBIReQRdhc_osBJ9yZyPic18VN2C-nKL-DYKZQlOGCBYdE37DaxnGSDq6CE_QzijvAA==)
41. [foundstep.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE7oE7ji3QE7jpYguc4x7thsMFsSCMuij3pLDRzrMpVAOKyTCtliee3slBmGrGko67mQVcvLAed-iBnBi0BBbCchSiQobmQ2MqJxjvRic1fbPwjKE8bnXIsfbIsVr5iSp-CzlQ76kHC_1Wz)
42. [livmo.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFa53sTu47skS7SxgtmKbYNT_GfYxJccOHdkZimk66V6y6dN3b98ehDUlNOiLA-oOpOmEgi-xb5aVn65PkrueGv4UUQ99q-fM3H4utI3LbRxDXSotv7cx6D2yK5CbOgTwP2DEE8p_pji7ZC)
43. [axial.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHBh7fz0pIKCCt-y-dAsY9nLW2oMcx-usJcn-yxJjs-dCT-HVs3SoXfnF8QBA27Cgr66PjgvSar4dGMhfSfzg-0DdUjvGCZDQwY-CjReQrFzRac59rrKSiHHSyjukbU6MQ=)
44. [carta.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEMtxfEHXaei8zQPuUiRwWEbggAqIt0jNQmFmvEm7Wjr7CFqwfno112sscSfwdcDYnSxJ8IgruMzvMfVgUGWfbBQpfNMpn9UZIrJYhdpTkcVbiJWc5XV_2EEcJpHognjv5auO4i0iOcg1-NzDkz)
45. [saas-capital.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQE14HHM6whPHgG87gtG5zQFa1O_mqXemlPMdJY0bdefJk9vcLGT2cNBjvS07mZHT5nYgIo9AKs5ylSis9NjR3K8QSkjs9rwsJx1XTM9E3enuDiNYmurc2rHeS2xBPNYxeQ8R9EBVnXj4eM8LlicDxrX7cJtBXVgvoLT)