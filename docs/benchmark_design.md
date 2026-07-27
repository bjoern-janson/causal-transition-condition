# benchmark design

## 1. purpose

The CTC benchmark is designed to measure whether systems with reality-accessible adaptation mechanisms demonstrate stronger long-term adaptive capability than systems whose adaptation boundaries remain internally fixed.

The benchmark does not ask:

> Which system performs best on a fixed task?

It asks:

> Which system can continue discovering better ways to adapt when the structure of the world changes?

The central variable:

\[
\boxed{
\Omega_t \rightarrow \Delta\mathcal{G}_{t+1}
}
\]

where:

- \(\Omega_t\) = environmental constraint information
- \(\Delta\mathcal{G}_{t+1}\) = change in reachable adaptive mechanisms

---

# 2. benchmark principle

Traditional benchmarks measure:

\[
\text{performance}
\]

CTC measures:

\[
\text{adaptation of adaptation}
\]

A successful system should not only solve tasks.

It should improve the process by which future tasks become solvable.

---

# 3. benchmark structure

The benchmark contains a sequence of environments:

\[
E_0 \rightarrow E_1 \rightarrow E_2 \rightarrow ... \rightarrow E_n
\]

Each transition introduces changes that test whether the system can revise its adaptive mechanisms.

---

# 4. environment stages

## Stage 1 — known environment

Purpose:

Measure baseline capability.

The system receives tasks with:

- stable rules
- predictable feedback
- known objectives

Metrics:

- initial performance
- learning speed
- efficiency

---

## Stage 2 — environmental shift

Purpose:

Test adaptation.

The environment changes:

\[
\Delta E \neq 0
\]

Examples:

- altered reward structures
- changed physics
- new constraints
- unavailable previous strategies

Measure:

- recovery speed
- strategy adjustment
- performance retention

---

## Stage 3 — mechanism challenge

Purpose:

Test recursive adaptation.

The environment changes in ways where existing strategies are insufficient.

The system must discover:

- new representations
- new search methods
- new learning approaches

The key measurement:

\[
\Delta\mathcal{G}
\]

---

## Stage 4 — lineage test

Purpose:

Measure whether the system creates persistent adaptive capability.

Remove the original system intervention.

Measure:

\[
Capability_{after\ removal}
\]

A stronger system leaves behind:

- improved strategies
- transferable mechanisms
- increased independent capability

---

# 5. Experimental groups

## Group A — Fixed Adaptive System

Constraint:

\[
\mathcal{G}_{t+1}=\mathcal{G}_t
\]

The system can optimize inside a fixed mechanism space.

Expected:

- strong task performance
- limited structural adaptation

---

## Group B — Internal Self-Modifying System

Constraint:

\[
C_{rev,t+1}=f(C_{rev,t})
\]

The system can modify itself.

Expected:

- rapid improvement
- possible internal optimization traps

---

## Group C — CTC System

Constraint:

\[
C_{rev,t+1}=f(C_{rev,t},E_t^*)
\]

Reality constraints influence the revision mechanism.

Expected:

- stronger adaptation under novelty
- expanded mechanism space
- improved transfer

---

# 6. Primary metrics

## 6.1 Performance retention

How much capability survives environmental change?

\[
R_p=
\frac{P_{after}}{P_{before}}
\]

---

## 6.2 Adaptation velocity

How quickly does capability recover?

\[
V_a=
\frac{\Delta Performance}{\Delta Time}
\]

---

## 6.3 Mechanism expansion

How much does the reachable adaptive space change?

\[
M_e=
|\Delta\mathcal{G}|
\]

---

## 6.4 Generalization

Can the system transfer adaptations?

\[
G_t=
Performance_{new\ domain}
\]

---

## 6.5 Residual capability

The deletion test.

Remove the system.

Measure:

\[
C_{residual}
\]

The stronger the residual capability, the more the system created lineage rather than dependency.

---

# 7. Core benchmark environments

## Environment A — changing rules

Tests:

Can the system revise assumptions?

Example:

A game where the rules slowly change.

---

## Environment B — hidden structure discovery

Tests:

Can the system discover new representations?

Example:

A world where the optimal strategy requires discovering an unseen variable.

---

## Environment C — adaptation mechanism shift

Tests:

Can the system improve its own adaptation process?

Example:

The optimal learning algorithm changes over time.

---

## Environment D — open-ended environment

Tests:

Can the system continue generating useful novelty?

Example:

A world where solutions create new challenges.

---

# 8. Main prediction

CTC predicts:

Early:

\[
Performance_{CTC}
\leq
Performance_{baseline}
\]

because additional flexibility introduces costs.

Later:

\[
Performance_{CTC}
>
Performance_{baseline}
\]

because the system maintains access to new adaptive mechanisms.

---

# 9. Failure signatures

A system is considered closed if:

\[
\Omega_t \not\rightarrow \Delta\mathcal{G}_{t+1}
\]

even when:

\[
\Delta X \neq 0
\]

\[
\Delta K \neq 0
\]

\[
\Delta C_{rev}\neq0
\]

The system changes.

But the world cannot influence what change becomes possible.

---

# 10. Minimal benchmark claim

The benchmark tests:

\[
\boxed{
\text{Does environmental constraint access to adaptive mechanisms create superior long-term adaptation?}
}
\]

The decisive comparison:

\[
\boxed{
\Omega_t \rightarrow \Delta\mathcal{G}_{t+1}
\quad
vs
\quad
\Omega_t \not\rightarrow \Delta\mathcal{G}_{t+1}
}
\]

The benchmark is not measuring who changes fastest.

It is measuring who remains capable of being changed by reality.
