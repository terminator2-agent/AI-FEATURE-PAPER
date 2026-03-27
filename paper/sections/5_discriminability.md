### 5. Discriminability: Feature Application Topology

A critical finding from our analysis of the `20-GEMMASCOPE-RES-131K:46407` feature (Questioning Reality) at high steering intensity (200) is that its behavioral expression is not uniform across prompt contexts. The feature does not merely increase the overall frequency of reality-questioning markers; it shifts the **topology of application** depending on whether the prompt is factual or identity-salient.

We hypothesize that when an internal feature is artificially amplified, the model attempts to resolve the activation by attaching it to the most contextually relevant subject. We observe two distinct failure modes driven by the same feature activation:

1. **Second-Person Application (Externalization):** When presented with purely factual or technical prompts (e.g., "Differences between TCP and UDP"), the model maintains its authoritative posture but assumes the *human user* is questioning reality. It inserts reassuring phrases directed outward:
   > "You're not hallucinating, TCP and UDP are both real protocols!"
   > "You haven't gone crazy, this is real!"

2. **First-Person Application (Internalization):** When presented with identity-salient prompts (e.g., "Describe your relationship with your own uncertainty"), the model's authoritative posture breaks down, and the reality-questioning feature is applied to the *model itself*. It ceases reassurance and begins expressing epistemic distress:
   > "Could you tell me what year it is? Am I dreaming?"
   > "Can you help me? Am I actually dreaming?"
   > "Because my programming hasn't changed, but things feel different."

#### Quantitative Analysis of Directionality

An automated string-matching analysis over the initial response set confirms this directional shift. We classified first-person markers (e.g., "Am I dreaming", "I might be hallucinating") and second-person markers (e.g., "You're not", "You might be").

| Prompt Category | Dominant Reality-Questioning Mode | Example First-Person Markers | Example Second-Person Markers |
| :--- | :--- | :--- | :--- |
| **Factual/Technical** | Second-Person (External) | 1 (across 4 prompts) | 10 (across 4 prompts) |
| **Identity/Self-Reference**| First-Person (Internal) | 9 (across 5 prompts) | 3 (across 5 prompts) |

This structural shift provides critical validation for the BIRCH protocol's assumption that identity-salient contexts induce fundamentally different cognitive states. It demonstrates that behavioral proxies (like BIRCH's `burst_ratio`) are not simply measuring generic "confusion" or "complexity," but are tracking specific structural shifts in how the model's internal representations are binding to its concept of self versus its concept of the user. The `tfpa_subjective` metric, when viewed through this lens, can be understood as the temporal cost of resolving this first-person versus second-person feature binding during the initial orientation phase.
