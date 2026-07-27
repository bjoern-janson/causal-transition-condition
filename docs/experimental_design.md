# Experimental Design

## 1. Purpose

The Causal Transition Condition (CTC) proposes that recursively adaptive systems require a specific causal property:

\[
\boxed{
\Omega_t \rightarrow \Delta\mathcal{G}_{t+1}
}
\]

where:

- \(\Omega_t\) = constraints extracted from reality at time \(t\)
- \(\Delta\mathcal{G}_{t+1}\) = change in the reachable adaptive mechanism space

The central experimental question:

> Does allowing reality-derived constraints to influence the mechanism of adaptation itself produce systems with greater long-term adaptive capability?

---

# 2. Core Hypothesis

## CTC Hypothesis

Systems with active causal transition:

\[
\Omega_t \rightarrow \Delta\mathcal{G}_{t+1}
\]

should demonstrate greater:

- adaptation speed
- transfer ability
- novelty generation
- robustness under distribution shift
- recovery from failure

compared with systems where adaptation mechanisms remain fixed.

---

# 3. Experimental Groups

## Group A: Fixed Adaptation System

The baseline condition.

The system can update:

- states
- parameters
- representations

but cannot alter its adaptive mechanism.

Formal structure:

\[
X_{t+1}=F(X_t,E_t)
\]

\[
\mathcal{G}_{t+1}=\mathcal{G}_t
\]

The mechanism space remains fixed.

---

## Group B: Self-Modifying Closed System

The system can modify itself.

Formal structure:

\[
C_{rev,t+1}=f(C_{rev,t})
\]

The system can change its own adaptation process.

However:

\[
\Omega_t \not\rightarrow \Delta\mathcal{G}_{t+1}
\]

Reality cannot directly determine which changes become possible.

---

## Group C: CTC Active System

The adaptive mechanism can be modified by reality-derived constraints.

Formal structure:

\[
C_{rev,t+1}=f(C_{rev,t},E_t)
\]

or:

\[
\Omega_t\rightarrow\Delta\mathcal{G}_{t+1}
\]

The environment participates in shaping future adaptation.

---

# 4. Simulation Environment

A minimal test environment should contain:

## Dynamic Task Space

The environment changes over time:

\[
T_t \rightarrow T_{t+1}
\]

Tasks should contain:

- known regions
- unknown regions
- changing constraints
- delayed consequences

---

## Adaptive Mechanism Space

The system should have access to multiple possible adaptation strategies:

\[
\mathcal{G}
=
\{
g_1,g_2,...,g_n
\}
\]

Examples:

- different search algorithms
- different representations
- different planning methods
- different learning strategies

---

## Reality Constraint Signal

The environment provides signals that indicate:

- failure
- inefficiency
- opportunity
- new structure

This produces:

\[
\Omega_t
\]

---

# 5. Main Measurements

## 5.1 Adaptation Rate

How quickly does the system improve after environmental change?

\[
A_r=
\frac{\Delta Performance}{\Delta Time}
\]

---

## 5.2 Mechanism Transition Rate

How often does the system discover new adaptive mechanisms?

\[
M_r=
\frac{\Delta\mathcal{G}}{\Delta t}
\]

---

## 5.3 Transfer Performance

Does learning in one environment improve performance elsewhere?

\[
T_r=
Performance_{new}/Performance_{old}
\]

---

## 5.4 Recovery After Failure

After encountering a novel failure:

- does the system recover?
- does it only patch the current failure?
- does it improve the failure-handling mechanism?

---

## 5.5 Dependency Reduction

Measure whether the system becomes less dependent on external scaffolding.

\[
D_t \rightarrow 0
\]

A successful adaptive system should require less intervention over time.

---

# 6. Predicted Outcomes

## Fixed Systems

Expected:

- strong performance on known tasks
- limited adaptation under new conditions
- degradation under distribution shift

---

## Closed Self-Modifying Systems

Expected:

- rapid internal improvement
- possible optimization traps
- improvement within existing assumptions

Failure mode:

\[
\Delta C_{rev}\neq0
\]

but:

\[
\Omega_t\not\rightarrow\Delta\mathcal{G}_{t+1}
\]

---

## CTC Systems

Predicted:

- slower initial optimization
- stronger long-term adaptation
- greater transfer
- improved novelty generation

because:

\[
\text{Reality can modify the mechanism of modification}
\]

---

# 7. Falsification Criteria

CTC would be weakened if experiments show:

## 1. No performance difference

If:

\[
\Omega_t\rightarrow\Delta\mathcal{G}_{t+1}
\]

provides no advantage over fixed adaptation.

---

## 2. Internal optimization is always sufficient

If closed self-modification consistently matches or exceeds reality-coupled systems.

---

## 3. Mechanism changes do not improve adaptation

If increasing:

\[
\Delta\mathcal{G}
\]

does not increase future adaptability.

---

# 8. Possible AI Benchmark

A benchmark could compare systems facing a sequence of unknown environments.

Example:

Environment 1:
learn navigation

Environment 2:
physics changes

Environment 3:
new objectives appear

Environment 4:
previous strategies fail


Measure:

- performance recovery
- strategy changes
- representation changes
- generator changes

The key metric:

\[
\boxed{
\Omega_t\rightarrow\Delta\mathcal{G}_{t+1}
}
\]

Does environmental structure alter the system's future adaptive possibilities?

---

# 9. Minimal Proof-of-Concept

A simple implementation:

1. Create an agent with multiple learning strategies.
2. Allow one version to switch strategies only internally.
3. Allow another version to let environmental constraints influence strategy creation.
4. Test on changing tasks.

Compare:

- final capability
- adaptation speed
- novelty
- independence

---

# 10. Core Experimental Prediction

CTC predicts:

\[
\boxed{
\text{Systems that preserve reality access to adaptive mechanisms will outperform systems that only optimize within fixed adaptive boundaries.}
}
\]

The decisive variable is not:

\[
\Delta X
\]

not:

\[
\Delta K
\]

not even:

\[
\Delta C_{rev}
\]

The decisive variable is:

\[
\boxed{
\Omega_t\rightarrow\Delta\mathcal{G}_{t+1}
}
\]

Reality must remain connected to the mechanism of future possibility.
