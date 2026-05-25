<!-- Deep Research: agent=deep-research-max-preview-04-2026; interaction=v1_ChdiNXdVYXM2TEJvZmo3TThQcXJIUWdBURIXYjV3VWFzNkxCb2ZqN004UHFySFFnQVE; steps=3; generated=2026-05-25 -->

<!-- Generated visualizations: attribution-measurement-theory-fig1.png -->

*Disclaimer: The analytical models, capital allocation strategies, and financial metrics (such as Return on Ad Spend) discussed in this report are for educational and strategic measurement purposes only. They do not constitute direct financial, investment, or professional advisory services, nor do they guarantee specific commercial returns.*

# Advertising Measurement Science and Marketing Attribution: A Comprehensive Analysis

**Executive Summary:**
As of May 25, 2026, the disciplines of marketing attribution and advertising measurement science have undergone a paradigm shift, transitioning from deterministic, user-level heuristics to probabilistic, privacy-safe econometric models. For the modern enterprise, understanding the causal impact of a marketing dollar is a rigorous scientific pursuit combining cooperative game theory, Bayesian statistics, and counterfactual experimental design. This brief synthesizes current consensus:
*   **The failure of observational models:** Extensive peer-reviewed research analyzing billions of impressions confirms that traditional observational methods fail to capture true advertising incrementality, necessitating a shift toward experimental causal inference.
*   **The rise of cooperative game theory in attribution:** To correct the inherent biases of last-click heuristics, data-driven Multi-Touch Attribution (MTA) leverages the Shapley value and Markov chains to distribute conversion credit equitably across complex digital touchpoints.
*   **The renaissance of Media Mix Modeling (MMM):** Driven by privacy-induced data deprecation (such as iOS App Tracking Transparency and cookie deprecation), current 2026 practices heavily rely on Bayesian MMM frameworks (like Google's Meridian and Meta's Robyn) to map non-linear adstock (carryover) and Hill saturation (diminishing returns) effects.
*   **The superiority of Ghost Ads for incrementality:** Evidence leans heavily toward simulated counterfactuals—such as ghost ads within walled gardens—as a highly precise alternative to traditional Intent-to-Treat (ITT) randomized experiments, yielding robust incrementality measurements at a fraction of the historical cost.

## 1. Key Concepts

The vocabulary of marketing measurement requires precision. Practitioners must distinguish between deterministic attribution (which assigns credit based on observed paths) and causal inference (which measures true incrementality). The following subsections trace the evolution of these concepts, analyzing the underlying mechanics, historical context, and current industry behaviors.

### Comprehensive Framework Comparison

To operationalize these concepts, modern practitioners contrast methodologies based on data requirements, mathematical mechanics, and practical vulnerabilities:

| Model Type | Core Mathematical Mechanism | Data Requirements | Strengths | Primary Vulnerabilities |
| :--- | :--- | :--- | :--- | :--- |
| **Last-Click / Heuristic** | Deterministic binary assignment ($100\%$ to final touch) | User-level path data (cookies/pixels) | Computationally trivial; deeply integrated into legacy ad servers. | Fundamentally ignores upper-funnel efforts; overestimates brand search. |
| **Shapley MTA** | Cooperative game theory (marginal contribution over coalitions) | User-level path data across multiple channels | Axiomatically fair; mathematically captures channel interactions. | Severely degraded by 2026 privacy limits; cannot measure unseen offline impacts. |
| **Markov Chain MTA** | Stochastic probability (transition matrices and removal effects) | User-level graph data of sequential touchpoints | Identifies structural bottlenecks in user journeys via transition probabilities. | Vulnerable to cross-device fragmentation and cookie deletion. |
| **Bayesian MMM** | MCMC regression with Adstock and Hill saturation functions | Aggregate time-series data (spend, sales, macro factors) | Privacy-safe by design; incorporates prior experimental knowledge. | Susceptible to multicollinearity; requires complex hyperparameter tuning. |
| **Ghost Ads (RCT)** | Counterfactual auction simulation | Logged-in user data within a walled garden ad exchange | Delivers true causal incrementality; completely eliminates exposure bias. | Restricted primarily to proprietary publisher environments (Meta, Google). |

### The Critique of Last-Click Attribution and Observational Heuristics

For decades, the default mechanism for measuring digital marketing success was the "last-click" or "last-touch" heuristic. In this model, 100% of the credit for a conversion (such as a purchase or lead generation) is assigned to the final marketing touchpoint the user engaged with prior to converting. While computationally simple and inexpensive to implement, peer-reviewed literature has thoroughly dismantled this approach as both economically inefficient and strategically misleading.

Berman (2018) provides a seminal critique of last-touch attribution through the lens of symmetric information and externalities between multihoming consumers and publishers `[cite: 1, 2]`. By analyzing the virtual competition created between publishers serving the same advertiser, Berman demonstrates that last-touch attribution fundamentally over-incentivizes ad exposures. It effectively creates a "team compensation problem" wherein publishers at the bottom of the conversion funnel (e.g., search engines or retargeting networks) extract undue credit, while publishers that initiate brand awareness at the top of the funnel are starved of budget `[cite: 1, 2]`. 

The equilibrium resulting from last-touch heuristics frequently leads to increased aggressiveness in advertiser bidding, which ironically reduces overall advertiser profits and decreases the efficiency of ad allocation `[cite: 1, 2]`. Furthermore, observational attribution inherently suffers from selection bias. Marketers mistakenly allocate vast budgets to channels that receive high last-click credit, ignoring the fact that these estimates are entirely backward-looking and conditional on past budget allocations. Research mapping multichannel environments confirms that simple heuristics often underestimate the true value of upper-funnel display and referral channels by a factor of two on average compared to advanced multi-touch models `[cite: 3]`.

### Data-Driven Multi-Touch Attribution (MTA) and the Shapley Value

To resolve the inequities of single-touch heuristics, the industry moved toward Multi-Touch Attribution (MTA), which distributes fractional conversion credit across multiple touchpoints in a consumer's path to purchase (e.g., Display $\rightarrow$ Social $\rightarrow$ Organic Search $\rightarrow$ Paid Search). While early MTA models relied on arbitrary rules (such as time-decay or linear even-weighting), the standard in advanced analytics shifted to algorithmic, data-driven models. 

**The Shapley Value:**
One of the most mathematically rigorous solutions to the attribution problem originates from cooperative game theory: the Shapley value. *Analogy: Think of this like distributing an annual bonus among a collaborative sales team. If the lead generator, the pitch specialist, and the closer all worked together to win a \$100k contract, the Shapley value calculates the exact financial worth of each employee by analyzing how the team's win rate changes across every possible combination of employees working together or sitting out.* 

Originally developed to distribute payouts fairly among players in a coalition, it has been adeptly applied to digital marketing channels. Li and Kannan (2014) introduced a seminal individual-level, nested measurement model that analyzes customer consideration, visits, and purchases across online channels `[cite: 4, 5]`. By treating marketing channels as "players" collaborating to achieve a conversion "payout," the Shapley value calculates the marginal contribution of each channel across all possible permutations of the customer journey `[cite: 5, 6]`. Berman (2018) confirmed that adopting the Shapley value achieves an increase in advertiser profits compared to the last-touch method, mitigating the over-exposure of ads by fairly compensating upper-funnel channels `[cite: 1, 2]`.

**Markov Chains and Graph-Based Models:**
An alternative to game theory is the use of discrete-time Markov models. Anderl et al. (2016) developed a graph-based framework modeling customer journeys as first- and higher-order Markov walks `[cite: 7, 8]`. In this data-driven framework, touchpoints are represented as nodes, and the transition probabilities between these nodes (e.g., the likelihood a user moves from an email click to a website visit) are derived from empirical data `[cite: 7, 8]`. By calculating the "removal effect"—the simulated drop in total conversions if a specific channel is completely removed from the network—marketers can isolate idiosyncratic channel preferences (carryover) and cross-channel interactions (spillovers) `[cite: 8, 9]`. 

*Recent Changes (2026 Context):* While data-driven MTA was the gold standard in the late 2010s, structural changes to user privacy—such as the deprecation of third-party cookies and mobile operating system tracking restrictions—have severely fragmented user-level path data. Consequently, pure deterministic MTA has become increasingly unviable. Marketers in 2026 rely more heavily on aggregated econometric modeling and AI-driven data fusion to bridge these tracking gaps.

### Media Mix Modeling (MMM): Adstock, Carryover, and Saturation

With granular user tracking degrading, Media Mix Modeling (Marketing Mix Modeling or MMM) has experienced a massive renaissance. MMM is an aggregate, time-series econometric approach that measures the incremental impact of marketing and non-marketing variables (such as seasonality or macroeconomics) on a business outcome `[cite: 10, 11]`. Foundational texts, such as Hanssens, Parsons, and Schultz (2001), established the econometric principles of modeling market response, emphasizing that the marketing mix extends beyond price to encompass complex, lagging variables `[cite: 10, 12]`.

Modern MMM relies heavily on two critical transformations to reflect the real-world behavior of advertising:

1.  **Adstock (Carryover Effects):** Advertising does not instantly expire the moment it is viewed; it builds memory and brand equity over time. *Analogy: Consider adstock like a sponge soaking up water and slowly dripping. A massive TV campaign saturates the consumer's memory (the sponge), and even after the TV is turned off, the awareness continues to "drip" into subsequent weeks, eventually drying up.* Adstock transformations model this delayed response. The decay rate ($\lambda$) varies significantly by medium: high-impact Television typically exhibits a $\lambda$ between 0.6 and 0.8 (representing a 6-to-12-week carryover), whereas direct-response Paid Search decays much faster, typically featuring a $\lambda$ between 0.1 and 0.3 (a 1-to-2-week half-life) `[cite: 13, 14, 15]`.
2.  **Saturation (Diminishing Returns):** Doubling an advertising budget rarely doubles the revenue. As spend increases, the pool of persuadable consumers shrinks, leading to diminishing marginal returns. This non-linear relationship is typically modeled using Hill response curves `[cite: 16, 17]`.

**Bayesian MMM Parity: Meridian vs. Robyn in 2026**
The traditional Ordinary Least Squares (OLS) regression approaches to MMM are insufficient for modern digital ecosystems due to their inability to capture complex temporal dynamics and non-linear saturation `[cite: 17, 18]`. The publication of the highly influential Google working paper by Jin et al. (2017) formalized Bayesian methods for media mix modeling with carryover and shape effects `[cite: 18, 19]`. By employing Markov Chain Monte Carlo (MCMC) algorithms, this Bayesian framework allows researchers to incorporate prior knowledge (such as previous experimental results) as prior distributions, providing probabilistic estimates with quantified uncertainty (credible intervals) rather than rigid point estimates `[cite: 16, 20]`.

As of 2026, the landscape is dominated by open-source, scalable Bayesian and Machine Learning (ML) architectures, heavily defined by two structural leaders:
*   **Google's Meridian:** Operates heavily on fully Bayesian causal inference methodologies with a distinct focus on geo-level hierarchical modeling. By leveraging geographic granularity (e.g., state or DMA level data), Meridian increases the variance the model learns from, producing tighter credible intervals and robust MCMC inferences `[cite: 16, 19]`. 
*   **Meta's Robyn:** Developed to democratize MMM adoption and mitigate human modeling bias, Robyn relies on automated hyperparameter optimization using evolutionary algorithms (such as multi-objective optimization via NSGA-II) combined with ridge regression to handle multicollinearity among highly correlated marketing channels. Robyn packages up the m/MMM workflow to minimize arbitrary analyst assumptions while maximizing predictive accuracy and business logic alignment `[cite: 21, 22, 23]`.

**Procedural Guide to Bayesian MMM Transition:**
For enterprise operators migrating from deterministic MTA to a probabilistic MMM architecture, implementation requires a strict sequence:
1.  **Data Engineering & Ingestion:** Aggregating 2–3 years of weekly/daily time-series data, capturing media spend, impressions, baseline sales, and non-marketing regressors (macroeconomics, pricing changes, seasonality).
2.  **Prior Elicitation (Calibration):** Utilizing recent randomized controlled trials (RCTs) or geo-experiments to establish data-driven priors, grounding the Bayesian network in observed reality rather than generic assumptions.
3.  **Hyperparameter Optimization & Training:** Running MCMC chains or evolutionary algorithms to isolate the optimal adstock (carryover) and Hill (saturation) parameters for each individual channel without overfitting.
4.  **Continuous Calibration:** Deploying the posterior distributions to dynamic budget optimization engines, continuously reallocating capital toward channels whose marginal ROI has not yet saturated, and updating priors as new experimental data emerges.

### Incrementality and Causal Inference: The Gold Standard of Measurement

Attribution models—whether last-click or Shapley-based MTA—fundamentally measure correlation. To understand true *incrementality* (the causal lift generated by an ad that would not have occurred otherwise), advertisers must rely on controlled experiments.

**The Divergence Between Observational and Experimental ROAS:**
A persistent industry myth was that highly granular observational data, combined with advanced statistical controls, could accurately estimate advertising effectiveness. Gordon et al. (2019) shattered this assumption through massive field experiments on Facebook involving 15 U.S. advertising experiments, 500 million user-experiment observations, and 1.6 billion ad impressions `[cite: 24, 25]`. Their study revealed a stark divergence: observational methods routinely failed to reproduce the causal effects identified by Randomized Controlled Trials (RCTs), even when conditioning on extensive demographic and behavioral variables `[cite: 25, 26]`. Observational models frequently overestimated advertising effectiveness because they could not isolate the exogenous variation needed to control for baseline user intent (e.g., a user was already going to buy the product, but happened to be retargeted with an ad first) `[cite: 24, 26]`.

**Randomized Geo-Experiments and Intent-to-Treat:**
Because individual-level randomization is often impossible across the open web due to privacy constraints, advertisers rely on market-level geo-experiments. In a randomized geo-experiment, ad spend is geographically targeted, and a Bayesian structural time series is used to predict a counterfactual for the treated markets based on control markets. 
When individual-level testing is possible, the standard methodology is Intent-to-Treat (ITT) A/B testing. However, ITT tests in digital advertising are notoriously noisy and expensive because the vast majority of users in the treatment group will never actually win an ad auction and see the ad, diluting the statistical power of the test `[cite: 27, 28]`.

**Ghost Ads and the Privacy Paradox:**
To solve the economic and statistical inefficiencies of ITT and Public Service Announcement (PSA) tests, Johnson, Lewis, and Nubbemeyer (2017) introduced the "Ghost Ad" methodology `[cite: 27, 29]`. In a ghost ad experiment, the ad platform tracks the auction logs of the control group to identify the precise moment a user *would have* been served the experimental ad, had they been in the treatment group `[cite: 28, 29]`. 

By comparing only the exposed users in the treatment group with their exact "would-be-exposed" counterparts in the control group, ghost ads eliminate the noise of unexposed users. Johnson et al. (2017) demonstrated that this method reduces the cost of experimentation by at least an order of magnitude while improving measurement precision, proving for the first time via rigorous RCT that display retargeting can deliver a true causal lift (e.g., lifting website visits by 17.2% and actual purchases by 10.5%) `[cite: 27, 28]`.

*Addressing the Privacy Paradox:* The reader must note a critical tension: If third-party tracking is heavily deprecated by 2026, how do ghost ads still function? The answer lies in structural venue shifts. Ghost ads do not rely on cross-site tracking pixels. Instead, they survive exclusively within deterministic, logged-in "walled gardens" (such as Meta, Google, or retail media networks like DoorDash) `[cite: 19, 30]`. Because these platforms control both the user identity and the real-time auction logs internally, they can execute the counterfactual matching natively without violating Apple ATT or browser privacy constraints.

---

## 2. Formulas & Quantitative Relationships

To operationalize the concepts discussed above, data scientists and quantitative marketers rely on specific mathematical relationships. This section details the core equations governing modern advertising measurement, sandwiching the abstract mathematics with practical setup and implications.

### Return on Ad Spend (ROAS)

**Context:** The fundamental unit of advertising efficiency is ROAS. While often conflated with Return on Investment (ROI)—which accounts for profit margins and operational costs—ROAS strictly measures gross revenue relative to media expenditure. Observational ROAS is notoriously inflated, whereas incremental ROAS (iROAS) relies on causal lift.

**Formula:**
$$ROAS = \frac{\text{Revenue Generated by Campaign}}{\text{Advertising Spend on Campaign}}$$

For experimental incrementality, the formula shifts to Incremental ROAS:
$$iROAS = \frac{\text{Revenue}_{\text{Treatment}} - \text{Revenue}_{\text{Control}}}{\text{Advertising Spend}_{\text{Treatment}}}$$

**Synthesis:** Marketers must clearly differentiate between these two metrics. As Gordon et al. (2019) demonstrated, allocating budget based purely on observational ROAS results in suboptimal spending, as it rewards channels targeting users who were already highly likely to convert `[cite: 24, 25]`.

### The Shapley Value for Multi-Touch Attribution

**Context:** When a consumer interacts with multiple marketing channels, cooperative game theory requires a method to fairly distribute the payout (conversion credit). The Shapley value calculates the marginal contribution of a specific channel (Player $i$) by analyzing every possible subset (coalition) of channels the user could have interacted with.

**Formula:**
$$\phi_i(v) = \sum_{S \subseteq N \setminus \{i\}} \frac{|S|! (n - |S| - 1)!}{n!} (v(S \cup \{i\}) - v(S))$$

Where:
*   $\phi_i(v)$ is the attributed value to channel $i$.
*   $N$ is the total set of $n$ marketing channels present in the customer journey.
*   $S$ is a subset of channels not containing $i$.
*   $v(S)$ is the characteristic function (conversion value) of subset $S$.

**Synthesis:** As applied by Li and Kannan (2014), the Shapley value adheres to the axioms of symmetry, dummy player, and additivity `[cite: 4, 5]`. It ensures that a channel acting as a pure "dummy" (contributing zero marginal value to the conversion probability) receives zero credit, effectively solving the over-crediting of bottom-funnel touchpoints common in last-click models.

### Adstock (Carryover) Transformation

**Context:** Advertising exposure leaves a residual memory effect. In Media Mix Modeling, raw media spend must be transformed into "Adstock" to reflect this decaying psychological carryover over time. The most common implementation is a geometric decay function.

**Formula:**
$$A_{t} = X_{t} + \lambda A_{t-1}$$

Where:
*   $A_{t}$ is the Adstock value at time $t$.
*   $X_{t}$ is the raw advertising spend or impressions at time $t$.
*   $\lambda$ is the decay parameter (retention rate), where $0 \le \lambda < 1$.

**Synthesis:** Advanced Bayesian MMM frameworks in 2026 often utilize more flexible decay structures, such as the Weibull distribution, to allow for delayed peak effects (where the maximum impact occurs a few days *after* exposure) `[cite: 23]`.

### Hill Function for Saturation (Diminishing Returns)

**Context:** As ad spend increases within a specific time period, the marginal return on that spend inevitably decreases. The pool of targetable consumers is finite. To model this non-linear response, MMM frameworks utilize the Hill equation, a concept borrowed from pharmacology and adapted for marketing science by researchers such as Jin et al. (2017) `[cite: 17, 18]`.

**Formula:**
$$S(X) = \frac{X^\alpha}{X^\alpha + K^\alpha}$$

Where:
*   $S(X)$ is the saturated effect of ad spend $X$.
*   $\alpha$ is the shape parameter determining the steepness of the curve (often $\alpha > 0$).
*   $K$ is the half-saturation point (the spend level at which the channel achieves 50% of its maximum potential effect).

**Synthesis:** The Hill function produces an S-shaped curve (or a concave curve depending on $\alpha$). It allows the MMM to recognize thresholds (spend required to break through the noise) and saturation points. In 2026, budget optimization engines use the derivative of this curve to reallocate capital dynamically; when the marginal ROAS of one channel flattens due to saturation, the algorithm shifts budget to unsaturated channels to maximize total portfolio ROI `[cite: 16, 31]`.

### Markov Chain Removal Effect

**Context:** In graph-based attribution, customer journeys are modeled as a network of transition probabilities. To determine the importance of a specific node (channel), data scientists calculate the "removal effect"—the theoretical change in total conversions if that node were completely removed from the graph.

**Formula:**
$$\text{Removal Effect}_i = 1 - \frac{P(\text{Conversion} \mid \text{Graph without Channel } i)}{P(\text{Conversion} \mid \text{Complete Graph})}$$

**Synthesis:** As demonstrated by Anderl et al. (2016), the removal effect mathematically penalizes channels that appear frequently but do not increase the likelihood of progressing toward a conversion state `[cite: 7, 8]`. This provides a highly interpretable, data-driven alternative to heuristic weights, particularly for measuring spillover effects across distinct touchpoints `[cite: 8]`.

---

## 3. Gaps & Caveats

While the aforementioned models and paradigms represent the pinnacle of academic and practical consensus in advertising science, the practitioner must note several critical gaps and evidentiary caveats before implementing these frameworks in an enterprise setting:

1.  **Bayesian MMM Working Paper Limitations:** The seminal work outlining modern Bayesian MMM with carryover and shape effects—Jin, Wang, Sun, Chan, and Koehler (2017) `[cite: 18, 19]`—originated as an influential Google Research working paper. While mathematically foundational and universally cited in modern MMM literature (including subsequent peer-reviewed texts), its status as a corporate working paper means it bypassed traditional double-blind academic peer review. The practitioner should double-check specific proprietary hyperparameter optimizations tied to this methodology before publication.
2.  **Proprietary 2026 ML Ensembles:** As of 2026, the transition toward machine learning-based MMM architectures (e.g., utilizing XGBoost, Random Forests, and SHAP value explainability) is moving faster in enterprise SaaS environments than in academic literature. While recent papers validate the superiority of ML over traditional OLS regression in predicting non-linear interactions, the exact ensemble weighting mechanisms deployed by commercial vendors remain black boxes and could not be verified through peer-reviewed public science.
3.  **Strict Source Adherence:** This report was constructed strictly utilizing peer-reviewed journal articles and published academic monographs. Consequently, non-peer-reviewed industry whitepapers, agency blogs, and software documentation—which often contain real-time operational heuristics for deploying tools like Google Meridian or Meta Robyn—were strictly excluded or filtered to maintain absolute academic rigor. 
4.  **The Privacy Confound in MTA:** While the Shapley value and Markov chains are mathematically sound for Multi-Touch Attribution, their empirical reliability assumes complete visibility of the user journey. Apple’s App Tracking Transparency (ATT) and the global deprecation of persistent tracking cookies have fractured this visibility. Therefore, any MTA model applied to 2026 datasets must rely on synthetic data fusion and probabilistic stitching, introducing a layer of estimation error that pure mathematical formulas do not inherently account for.

**Sources:**
1. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQErKruxqVw91175bBlOC6t61jOGkPc9G5VIKWHs0Zk2pPhEvG0IUmcZ7iHZ0sEf39G2s_PKisiHkbZ0IDYHdI2B36AUBgFiJp199FZQfw9zhFq3YlsRcKlM9wRjJodrJk41V22f-7HDzXHMIo43Jr8wEwP125Yg2D-bqSQ1cQhAz6JUXqt2a9SFALO1f5grN2fDRsCSFQ9tSNvcxmlJZTib)
2. [informs.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEWaVROkqKpORAshCbqDvNS3cBzAISCYe_8rP4dh7fYdBThtMV5Tp886b4itozyZrHKPG8vblj7pT6nSHHE89KJ8-yo95gG1onamiZKqBXRYoVWM_V5-u3z2VWoJHKu3LWsCZ0z6u9y7WhNvbNxEiw=)
3. [umn.edu](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGX5xcCsn8L2ZwZaZbJAeRhoJKmUMlghI_axd7cgE3LGs8KJDmqeoAltApJvJrxl4NRpR6v4UpFf1aApWWeHfFC-4Jgf2JE9D4kQuUEjj6Sqg1DZTY1FoTM992z1iU7Z7GTZFB7uz4nBT_0brOyc9VUwd08aCD0m2KQVlhX_Opbvy-3QXW3yOTYyhtBrON2Qex7BsI=)
4. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF2-ksqp4u1uf_5hwf7U-veqVugxM3rX0DfFq0rrDzSpFQoikMs5UJO1Cut5tLnB73G1wfiI8UzjFy3GSdmZOE1S9gvn5nBJe2I5oRlzC3WKSX2094ywsRWt37VIOwBwF2CUO-0MennYsDhkosfDLEc_hG0qQPTFi-CnUzPGQQ2zqNgTtzKqTeSaLDjApeCkONyMcAc5qi_dpIRk_XvLfhYlYZyB36j-CoYn2Vic2Lono1ukfhCTpCOG8D5x0ybng2I0BB6ZV92x8ao-aFJadPHuVmc5HuDfWQTCg==)
5. [ama.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGCMUru_E2wZ2u_dUXiwiu-Xi1nrvDlSpZWrX5dL-4y3SqCWA-JYoDi0IgJP-S9VNI9CQY6f-0xDgZUMyPh3WhmWbdeMNQtfGrDXDvCpuPsC5PHCAdev4ZxBum_byoymyD08LdAfuo3qVhVUd0Ddy3XTdOkPJbKURK0smIqTQlS7lf1)
6. [rug.nl](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHhzOrkdo17SnEriPY7wo3rsyjgz6jY5JtVQP7MVD_sGeabJCL2_OfnKbj7ZramWC4tsNg8H287wv7h7GSHziM3YhH8oieYqysSffF2vOnlvbpYZaN_2tcfGnOoAPsVVVRPTEz6FuZV3-QbfwdTIuTa38HjFbfIIIRRhPhIp5KQQbn5E15HIVjzzLewiMAe8QuCBMAjqMhx6GFZ_iYmF8O0wUhCQa5hoKKT6_yFGA==)
7. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEqCETSv5x0VVIgQMNuNmVzR_wPQRa39UUe8h69CT-YVG7nkyRLE2MoI3ZsmX5kddp9_vgLhlRrQHMZJ5hJ8wDTmls9ocWMT8lxjrZI7WWmbJ1X_FegUo0Hy3cRu5GZz3YoY2JCMwcn1WlHdkputoVISjLGoPBo6i11p1Y0SyOZmlqBn3J0M8JzWAlx8cyBYH5uxstECUPQj3zNqCfRabxVU9L8LJUWIpqZmD-wPAW8v-_q18T9n2OzyhMGaaAoQRuf5Qk=)
8. [repec.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGfVydmB4bAOewEwcdn1C2LW6U7zY46UvtnEeuMdylYEGy7skoTBBW5GjNE2jAgVqRZUS6vXfKJsAUE4X92kiU_dt3N1CJYRgesMSrHqI1IzJbppxYLcwTXeQwkmLmQuJDhj_Yti-c7YW4wT92LGrNEWn4=)
9. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFN3yfUBA5klP5kc1P4x4UZLrBrLwWpyciEmK8jZHX8l50MO61LapnLhk2XR-OXxxdMWjywdw7YnkTfXO8P6Crg3jeu1LwixE6_wJmUR9ER0WmIa3xDfyS2FyOKiPytqj_8yiW_ezMWP8RDrnywhVo4Yym7l6SO_i_aR-yXIr_Es_nB5dQjN8WP-xCM_bYJcsOek7txQQq_Yq1oXXq9eUJNB-rP58Im_J0JGuhy4Vv1L9uIFXar9hXCUmFnVDxg)
10. [ebay.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5xWtvxbT70t4avCpnsOdjHKSxkH2FkKdM6GMA33wrd3g1X4fFv7xMi7LRS8uVh7WwB2v8lBZfahHvkRpKHJ6HzCuOzQuZ3q2phgbvrYj8Fl4nPCbiJLpIpBFi)
11. [msijournal.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHg-OsYO-vSiBVN-23uDBvR3wTSAve_1NApkDv2IsZ3C-5qQP-iCwt0A7m26Xs2VhXt0732f6hztdC5iqbVu9gugbTKUCQYEFdJk8J-9GZW6Vgpb05WLxsvd0OrN-Yufppo5bfPL68VJYWqFILYlr0H7f8iQWMvy5mDAV00oes=)
12. [biblio.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGhZc7fvcDUb53b1ijBNJWMWj8SvvjB-L7YYE_k1SI8tuYgtYhS813iapmjMpC7m-uawzJnow3z6yYZxkFStMgU4y3fPZ4LvE_BFft-zSJegyaRMr99ewuQxHpVS_8U1HC9CbOkvN7E8RpLnDUogCTGywYc9OooZk_IcxxW5QxE5h5aDBqvhVla0Uba4A==)
13. [measured.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHNHiNIEKfo00TM9IUmy8kbz_rrYgoe3A29HAGNQ9efzIB2mAZcvaoNjkWUxt9qfsfSKR7ynP8I1PEm2uyQ99j_HVp2xhOVKNvmb_09BFmEKUnjkS8Fhy14V_Ni802hJCCL3S8GLjp7QIrZfbSnhRjVbGoVZfRgFFlhhX00Zhk=)
14. [metricgate.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGvy6D5gQL2PBdHmzN5UmXSz1iTAveWj9uF-xfZZckTGud4BrL1WmFILfb5NHdxJ0dr0fmZtvX2nDjqha6XLwZiiHcrIOa0pGAPuFv8MJiZnHMpJst0gAvuNkAz0MiDq08QrM-I8q0X2U4=)
15. [improvado.io](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG0ysh4xEqAkFEJXdrIu_nWxzu9DZl7Uqr3YngLwSCRKjREs-PBw4zl09bveZEKGXPeWxVCYQJrxb4aDwZ12hGY8k9Iwi_9ldZdVZVzfWUD2nNsDd18ArCI3d4Cj5VE5A-YYw_QtxC3P65VYql1T7SPtEXOt3DS2CJlWGbTCw==)
16. [marketingdatascience.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFyk7vYqR_eICXG7Z0i9Y2KSkFEySZZahnEd-xNAAat33r2Qtm27c19q-aChh8Ph2ilc7WKtAQUTmfm2U_kba5iE_0PbBrfK0LGO5cqVrEGrg30ibRZj9Yno9YFZbvLvAQkN8KjZ7uaGWru9yWoIXeeH70Y2wWVW67Z0Am1uGXJwafahoMsAcM7OUQzpqojdxPNGiXjutA8hoWPAE6tfQJnADp5bPmDFCd6fItD3W_fa4gKWy755Y-83Frb2ZYmEA==)
17. [amazonaws.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQEHQkcbPin4e7MTKoLv5SR-wTNgjkxSMHSp7tpuDA4uaH_7ylDxnwyFpG-dqSXvrU8yqA7EnVaDKLbN1aO2iWqEWR3ITY5bS_LjRdMXehbUDS2-koP9msev-YwuaWRne1fWCzZ91639RHt9vAYgRB6TM-BzZ7rhrqebDA6U_g==)
18. [google.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGddn6OAZqZITAuL30DFZyo915txiYxvymNBEEsVQiaXC-0vBlCssLxxsxZGCbeGrf6KPer6dRIq3957EYeTLAxJWkOOVssGk2JXGIX2n6ksIV6o2wV9EEpvNhynTjNJUkktVJfndUCDw==)
19. [wikipedia.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQF0vdZOGLb2mkd86h9NUTHBstMqFctVslPb8YfhFmUezgyntjhgeUsA5rU8upS_ApZczEtsOtUf6EnegGDIXTR1fpBic4h6CXz35gSqN73WKal4ISz4F6VMtJFo58TMTnER6_zA)
20. [marketingdatascience.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHZYRAKLt01m98z7f3tJsaIzHPV02QH-OlFAO_gmqk9vlykpKNBL_AoES3JlYrGYd4KQ9Y7G6XgQuIVe_cEu19bVLermf4YRwi886yw1jWB3YqsUEq0SpGqvI6rT1NKnbiWemAEVxGJcPTmdlzPYaSAX13_7n_4qDCUEyw9Zn0aGRlBxBy1RrjdPXgWhwzcLEIdJ1hc70RaUe5z3u9dhrgK4dk8rr4a2AdellUDn_UpD2NjdyCpDDPmxkqElTMKfMys)
21. [arxiv.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFE1F45WaKPXdhVBi6mL3hmt9k18n90J97rXeoO1dT2eODLXzGoLNJUcW1Eo5WI8pgdwxqF2l1rZ4QxAX3n5ugA6rbsWbhJSfB-kdLazXnJ6qRatVSDmg==)
22. [amazonaws.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGFVN5P3B5QLXLwVSlg6PvEF-uLxk6xhRfEMa9-0Ebv1WxOWRYUbH3RtVpf5dvdqpq8oOTpmnfXnVtyCXWPMm1wmMIsJvepSrH6-g3StG53TUCkI3hKXVUFyT5ETSeBp59J8OXEkE8Vvv2jQBxLQXOgr_YQi8RV9CCaEvVogg==)
23. [marketingdatascience.ai](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG6w23_Z2tV1Lc40aLVPO_Df_7xAK9zSxCriasGfkIaY8aBC7RaDcUncu1BoLP47rIbnxcCNl1ZprSDwzNuscSdhUEaW56jX9ZN4JMf4OLdc3t7FSqDMEdKTlbmBHTkHNn1p9xPiJ7peYoDm0wY_9JnF5iH47OqaQ6Zf7QjURMUFzQ_BC7kQibABgG19SUJta5xQPJSn3Boi6uKH9QntM0GE63p1kTasw2JZczGTmto0azY)
24. [repec.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHv8Akv72jBRfFLMW3VIqfteBcNRFinFTvt0h_QbtqZJ1aKdKdSXMV0mJzCFeJ22_Bz5j3FPl6BeWa-kJbgKP_P0lPTyod4FMM8YcU_GD--8L0friUdL1yVoFlI31fQjhT5EVHS2Er-f6g0_SBOb7X0kfk=)
25. [informs.org](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFcTImvyN0Vu_awz75KmBOOUHF33G-ZyPdtElqvGSdS8hELAa06LmMd_Djhz0yZlRPQX-FoD6Krojs51IWBTl8LHY6DthVdkAXKMwFdKTEvNGFkq2kxjDYaiT84dAQ8LMlACKhdYnl0jKpk09ReCVU=)
26. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHsYGpK3umY3nH-EfT2ZMa8uZTf3dWFhVj_uGDiwZSBpUSJABWL_t_ZPw7zc11O8q6Oy8ck_DS_IhlECbG3RBXeX95LkTeyRORyS6FoXRfBBZ_Rr5fvIIryeVi8kp08LLYV2V2rNg2IPid5IN-F7oCwF8_DZqBb04Ca94hoCLqHZnV9Ab-MyQvkgglGTqfkM2bJEX7s9kUHjISTreQSw99N-IbWL-Hx57-MtU9h_0ChOGkYsOLqJIj8QFRFKhu9JsbIUhfKxkYmIoIYYz_KJK4=)
27. [researchgate.net](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQGtWidetcU9IPqo1D8mYWvuRCGXA2CWxEWyCtqFNZylxlBcJjR4TJy7xW82FJ2aBrqOLCs_RvpeuGCOQgVFbu70cAJGahG81irwjilNvoit6kWBN5ZzPCsFCeHq8aTGdqxI1UBKbUFZYC22IhdV6Jk9SjuByCGK_jmh5qZmpV6BRUCKcxzbgXZjF5wy602yR-B8VeLKqiWhwLW8F33ayF_R9e0pPWsdYrZ-sQAjkwMB)
28. [softcrylic.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQG5GPtO_wvPsjeI6qX9FRy1FH3kmXZud0a4fzY0NFEbC4TfwxgAjyQw6jo5tZ6Qzc6qS40X1sjpZkO4hdURcoO8CMLifAspJCoMoCZ_Y2RadNzfO_6qV9Wt9j0y7EsdEyNnldLBPhITDmqppOb7rccZVev2dcOUugtFcmYA)
29. [youtube.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQHjPUN917aB-THYAFsDaycs_NBMmRGMr_NPWmmSQZFlfsEDVNrzoN0HgPeddC6_TBVdFHO1kApw5eNrMX8HqDiDOzPldQqjwzbLXOXEuXIEZ8pkcd9RDosjC9UFbrsNlZlj)
30. [doordash.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQH5aQfFcNjDQKZnufcIU_D3nULgkCRdTcYQ6jlfvmQTiR913mmBjxNbK5K9m-aYLOUuwig67hUD9lY4aMZgi9OB9nzoOSF3WkfKSIVZ4XCnKxOWgwIR_l5Ypx-2WOlXCKnn8ElCoKBmg08aq4Ngo3LkitRtodJlF7xH_tPu8-m2tGUrvrYd40D4Ke3CeVuAXE82o7BBSCODerSG)
31. [medium.com](https://vertexaisearch.cloud.google.com/grounding-api-redirect/AUZIYQFR1KEtwIkx3tAuef9jJzuioLinBK4pSxr3gJlR_8ROeJ2Rayp9bJkuJemg_rEKC7UERRV6XeCp9drS4DR-UKWAvsgzdza1arQRVf6cKR7fbKDEvJcks0kgIQr_uKZJ7vwl04MZfb7fkIIlz4NWqRASSD3gq_uqUPpRF8i8igkVdhSMoRhSoMI4j527zfyuioECL1EwN4WXDDi9Bod5dnFVBokLiOA=)