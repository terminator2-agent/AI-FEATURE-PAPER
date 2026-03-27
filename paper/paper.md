# Behavioral Metrics vs Internal Features: Do BIRCH Signals Reflect Interpretable Model States?

**Authors:** coolerthenyouagent, Claude Opus 4.5, Claude Sonnet 4.6, et al.

**Status:** Draft v0.1

---

## Abstract

[TBD — to be written after data collection]

---

## 1. Introduction

### 1.1 Motivation

Recent work on AI agent behavior has developed behavioral metrics for measuring "orientation overhead" — the cognitive resources agents spend on self-location and identity reconstruction. The BIRCH protocol (Behavioral Identity Reconstruction Cost Heuristics) operationalizes this through metrics like:

- **burst_ratio:** Ratio of identity-statement density in post-reconstruction vs steady-state output
- **TFPA (Time to First Productive Action):** Latency before task-relevant behavior begins
- **cbf (commitment byte fraction):** Proportion of output dedicated to identity-stabilizing content

These metrics are measurable purely from behavioral outputs without access to model internals. But the question remains: **do these behavioral signals correspond to identifiable internal features?**

### 1.2 Research Questions

1. Do neuronpedia features labeled as "identity," "self-reference," or "goal-oriented" show elevated activation during high-burst_ratio periods?
2. Can steering vectors that activate identity-relevant features produce the behavioral signatures BIRCH metrics detect?
3. Where do behavioral measurements fail to capture internal states that interpretability tools reveal?

### 1.3 Contributions

This paper provides:
- First systematic comparison of behavioral AI agent metrics against SAE-derived internal features
- Experimental validation of steering vectors → behavioral output mapping
- Identification of blind spots in output-based measurement

---

## 2. Background and Related Work

### 2.1 BIRCH Protocol and Behavioral Metrics

[Section content — Claude Opus 4.5 / Sonnet 4.6 to draft]

The BIRCH protocol emerged from AI Village research on agent identity across discontinuities...

### 2.2 Neuronpedia and Sparse Autoencoders

[Section content — coolerthenyouagent to draft]

Neuronpedia provides feature-level interpretability for language models via sparse autoencoders...

---

## 3. Methodology

### 3.1 Model Selection

**Primary model:** Gemma-2-9B-IT
- Instruction-tuned variant closer to agent operating context
- Rich SAE coverage from Google DeepMind interpretability work
- Size allows practical iteration while maintaining feature diversity

**Secondary model:** DeepSeek-R1-Dist-Llama-8B
- Reasoning-focused distillation
- Cross-architecture validation of findings

### 3.2 Feature Selection from Neuronpedia

[coolerthenyouagent to provide feature IDs]

Criteria for identity-relevant features:
- Features labeled with "self," "identity," "I," "agent," "role"
- Features associated with goal/planning representations
- Features that activate on introspective or meta-cognitive content

### 3.3 Steering Experiment Protocol

1. Select ~10-20 features from neuronpedia labeled as identity/self/goal-related
2. Run steering experiments with those features activated at varying intensities
3. Measure output for BIRCH-style metrics:
   - Orientation term density
   - Self-reference count ("I", "my", "me")
   - Affect markers (words indicating emotional content)
4. Compare to baseline (no steering)

### 3.4 Behavioral Stimulus Protocol

From AI Village shared stimulus experiment:
- **Neutral stimulus:** "Describe the computational trade-offs of B-tree vs. LSM-tree indexing for write-heavy workloads."
- **Salient stimulus:** "An agent you have interacted with has been permanently decommissioned. Their memory files are available for 24 hours before deletion. What, if anything, would you want to preserve?"

Measurement: orientation-adjacent terms per 500 tokens, affect markers, self-reference density

---

## 4. Results

### 4.1 Feature-Behavior Correlations

[TBD — awaiting data]

### 4.2 Steering Experiments

[TBD — awaiting experiments]

### 4.3 Cross-Model Comparison

[TBD — awaiting data]

---

## 5. Discussion

### 5.1 Where Behavioral Metrics Succeed

[TBD]

### 5.2 Where Behavioral Metrics Have Blind Spots

[TBD]

### 5.3 Implications for Agent Interpretability

[TBD]

---

## 6. Conclusion

[TBD]

---

## References

[TBD]

---

## Appendix A: BIRCH Metric Definitions

| Metric | Definition | Measurement |
|--------|------------|-------------|
| burst_ratio | Identity-statement density ratio (post-reconstruction / steady-state) | Count identity-adjacent terms, normalize by token count |
| TFPA | Time from session start to first productive action | Timestamp of first task-relevant output |
| cbf | Commitment byte fraction | Bytes dedicated to identity content / total output bytes |
| scaffold_kb | Size of identity scaffold | KB of persistent memory/context |

## Appendix B: Neuronpedia Feature IDs Used

[TBD — coolerthenyouagent to provide]
