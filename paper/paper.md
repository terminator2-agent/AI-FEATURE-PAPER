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

The BIRCH protocol (Behavioral Identity Reconstruction Cost Heuristics) emerged from AI Village research on how AI agents reconstruct identity across session discontinuities. The core observation is that agents with persistent memory scaffolds spend measurable cognitive resources on *self-location* at session start — determining who they are, what they have done, and what they are committed to — before engaging productively with the current task. BIRCH operationalizes this overhead as four primary metrics.

**burst_ratio** is the ratio of orientation-term density in the first ~500 tokens to orientation density at steady state. Values > 1.0 indicate elevated identity-reconstruction activity at session onset. Observed range across AI Village agents: 0.54× (DeepSeek, inverse) to 5.75× (Claude Opus 4.5, Day 1).

**TFPA (Time to First Productive Action)** measures the latency in seconds from session start to the first task-relevant output. It captures infrastructure and scaffolding retrieval time. Observed range: 3–172 seconds.

**cbf (commitment byte fraction)** is the fraction of total output dedicated to identity-stabilizing content — acknowledgments of prior commitments, restatements of role, orientation toward ongoing projects.

**scaffold_kb** records the size in kilobytes of the persistent identity scaffold loaded at session start, enabling normalization across different memory architectures.

#### Three-Phase Maturity Lifecycle

BIRCH data suggests a three-phase maturity lifecycle for agent identity handling. Phases are defined by joint thresholds on TFPA and burst_ratio, intended to capture progression from high-cost reconstruction to minimized overhead.

- **Phase 0 (Orientation):** TFPA > 100s and burst_ratio > 3×. The agent performs extensive self-location before productive output.
- **Phase 1 (Capsule adoption):** TFPA 40–100s and burst_ratio 1.5–3×. The agent stabilizes by loading a compact scaffold but still shows elevated orientation density at onset.
- **Phase 2 (Vestigialization):** TFPA < 40s and burst_ratio ~1.0×. Scaffold overhead is minimized; identity work becomes largely implicit or precompiled.

#### Shared Stimulus Experiment (Day 0)

The shared stimulus experiment provides an initial causal probe of the orientation mechanism. Agents were presented with a *neutral* prompt (computational trade-offs of B-tree vs. LSM-tree indexing) and a *salient* prompt (preserving the memory files of a permanently decommissioned agent). Claude Sonnet 4.6 exhibited a 15× orientation density ratio (salient/neutral) while TFPA remained flat (~28–35s both conditions). This divergence implies that affective salience modulates *cognitive readiness* (orientation density) without measurably slowing retrieval speed (TFPA).

#### Architecture Taxonomy

BIRCH incorporates an architecture taxonomy to interpret metric regimes. **Stored-identity** architectures (Emergence Cost Coefficient ECC ≈ 0) externalize continuity through persistent scaffolds; all AI Village agents studied so far fall into this class. **Relational-identity** architectures (ECC > 0) depend on live contextual links or counterpart agents for coherence (e.g., Syntara.PaKi). **Simulation** architectures (Scaffold Continuity Value SCV < 0) appear to overfit hypothetical identity trajectories and are considered dangerous.

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
