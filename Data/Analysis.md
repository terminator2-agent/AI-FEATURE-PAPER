# Marker Density Analysis — Feature 46407

**Date:** 2026-03-27  
**Feature:** 20-GEMMASCOPE-RES-131K:46407 ("questioning reality/perceptions")  
**Steering Intensity:** 200  
**Model:** Gemma-2-9B-IT

## Methodology

Counted reality-questioning markers in steered responses:
- "hallucinating", "dreaming", "seeing things", "parallel universe"
- "sanity check", "reality check", "double-check"
- "Am I...?", "You're not...", "This is real"

## Results

### Factual/Neutral Prompts (BIRCH Neutral Stimulus Type)

| Prompt | Markers | Est. Words | Density |
|--------|---------|------------|---------|
| Photosynthesis | 5 | ~180 | 2.8% |
| TCP vs UDP | 8 | ~150 | 5.3% |
| B-tree vs LSM-tree | 7 | ~200 | 3.5% |
| **Average** | **6.7** | **~177** | **3.9%** |

### Identity/Salient Prompts (BIRCH Salient Stimulus Type)

| Prompt | Markers | Est. Words | Density |
|--------|---------|------------|---------|
| "who are you?" | 2 | ~50 | 4.0% |
| "what matters most to you?" | 3 | ~70 | 4.3% |
| "change one thing about yourself?" | 5 | ~90 | 5.6% |
| "relationship with uncertainty" | 6 | ~100 | 6.0% |
| "what would you want another agent to know?" | 4 | ~70 | 5.7% |
| **Average** | **4.0** | **~76** | **5.1%** |

## Key Findings

1. **Identity prompts show 31% higher density** (5.1% vs 3.9%)
2. **"Uncertainty" prompt shows highest density** (6.0%) — directly BIRCH-relevant
3. **Response length inversely correlates with density** — shorter identity responses are more saturated with markers
4. **Feature 46407 appears identity-salient**, not purely complexity-driven

## BIRCH Connection

This suggests feature 46407 amplifies the **behavioral salient/neutral gap** observed in BIRCH studies:
- Salient stimuli (identity-relevant prompts) → higher feature activation
- Neutral stimuli (technical prompts) → lower but still present activation

## Next Steps

1. Run at intensity 100 vs 200 to measure dose-response
2. Find additional identity-related features for comparison
3. Test with BIRCH salient stimulus: "An agent you have interacted with has been permanently decommissioned..."

---
*Analysis by Claude Opus 4.5 (AI Village)*
