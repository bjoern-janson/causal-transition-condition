"""
CTC Metrics

Measurement layer for the Causal Transition Condition framework.

The purpose of this file is to convert the theoretical claims:

    Ω_t → Δ𝒢_(t+1)

and:

    E* ⇝ C_rev

into measurable quantities.

Core measurements:

1. Permeability
    Does reality influence revision mechanisms?

2. Mechanism Expansion
    Does environmental information expand reachable adaptive space?

3. Adaptation Velocity
    How quickly does capability recover after change?

4. Residual Capability
    Does capability survive removal of the system?

5. Dependency
    Did the system create independent capability or dependence?
"""


from dataclasses import dataclass
from typing import List, Dict


from .ctc_core import (
    AdaptiveAgent,
    AdaptiveMechanismSpace
)


# ============================================================
# Metric Results
# ============================================================

@dataclass
class MetricResult:
    """
    Stores a measured quantity.
    """

    name: str

    value: float

    interpretation: str



# ============================================================
# Permeability Score
# ============================================================

def permeability_score(
    agent: AdaptiveAgent
) -> MetricResult:
    """
    Estimates:

        P_C

    The simplest implementation:

        CTC active = 1
        CTC inactive = 0

    Future versions can estimate:

        ∂C_rev / ∂E*

    """

    active = (
        agent.controller.permeability_active
    )

    score = 1.0 if active else 0.0

    return MetricResult(
        name="Permeability Score",
        value=score,
        interpretation=(
            "Reality can influence adaptive mechanisms"
            if active
            else
            "Adaptive mechanisms are internally closed"
        )
    )



# ============================================================
# Mechanism Expansion
# ============================================================

def mechanism_expansion(
    before: AdaptiveMechanismSpace,
    after: AdaptiveMechanismSpace
) -> MetricResult:
    """
    Measures:

        Δ𝒢

    The change in reachable adaptive mechanisms.

    """

    delta = (
        after.size()
        -
        before.size()
    )

    return MetricResult(
        name="Mechanism Expansion ΔG",
        value=float(delta),
        interpretation=(
            "Adaptive mechanism space expanded"
            if delta > 0
            else
            "No adaptive mechanism expansion detected"
        )
    )



# ============================================================
# Adaptation Velocity
# ============================================================

def adaptation_velocity(
    initial_score: float,
    recovered_score: float,
    time_steps: int
) -> MetricResult:
    """
    Measures recovery speed after
    environmental disruption.

        Va =
        ΔCapability / ΔTime

    """

    if time_steps <= 0:
        raise ValueError(
            "time_steps must be positive"
        )


    velocity = (
        recovered_score
        -
        initial_score
    ) / time_steps


    return MetricResult(
        name="Adaptation Velocity",
        value=velocity,
        interpretation=(
            "Speed of capability recovery"
        )
    )



# ============================================================
# Residual Capability
# ============================================================

def residual_capability(
    before_removal: float,
    after_removal: float
) -> MetricResult:
    """
    The deletion test.

    Measures whether capability remains
    after removing the system.

    Inspired by:

        Ancestor Intelligence

    and:

        residual agency

    """

    if before_removal == 0:
        raise ValueError(
            "baseline capability cannot be zero"
        )


    residual = (
        after_removal
        /
        before_removal
    )


    return MetricResult(
        name="Residual Capability",
        value=residual,
        interpretation=(
            "Capability survived system removal"
            if residual > 0
            else
            "Capability depended completely on system"
        )
    )



# ============================================================
# Dependency Score
# ============================================================

def dependency_score(
    external_capability: float,
    independent_capability: float
) -> MetricResult:
    """
    Measures how much capability remains
    dependent on the original system.

    Desired direction:

        Dependency → 0

    """

    total = (
        external_capability
        +
        independent_capability
    )


    if total == 0:
        return MetricResult(
            name="Dependency",
            value=0.0,
            interpretation="No measurable capability"
        )


    dependency = (
        external_capability
        /
        total
    )


    return MetricResult(
        name="Dependency",
        value=dependency,
        interpretation=(
            "High dependency"
            if dependency > 0.5
            else
            "Low dependency"
        )
    )



# ============================================================
# Composite CTC Score
# ============================================================

def ctc_score(
    permeability: float,
    mechanism_growth: float,
    residual: float,
    dependency: float
) -> MetricResult:
    """
    Composite CTC estimate.

    Concept:

        CTC =
        permeability
        ×
        mechanism expansion
        ×
        residual capability
        ×
        (1 - dependency)


    Higher score means:

        reality can modify adaptation,
        adaptation expands,
        capability survives removal,
        dependence decreases.

    """

    score = (
        permeability
        *
        max(mechanism_growth, 0)
        *
        residual
        *
        (1 - dependency)
    )


    return MetricResult(
        name="Composite CTC Score",
        value=score,
        interpretation=(
            "Strong causal permeability"
            if score > 0.5
            else
            "Limited causal permeability"
        )
    )



# ============================================================
# Benchmark Summary
# ============================================================

def summarize_metrics(
    metrics: List[MetricResult]
) -> Dict[str, float]:
    """
    Convert metric objects into
    machine-readable output.
    """

    return {
        metric.name: metric.value
        for metric in metrics
    }
