"""
CTC Core

Core implementation of the Causal Transition Condition (CTC).

The central hypothesis:

    Ω_t → Δ𝒢_(t+1)

where:

    Ω = environmental constraint information
    𝒢 = reachable adaptive mechanism space

A system satisfies CTC when reality-derived constraints
can influence the mechanism responsible for future adaptation.

This file defines the minimal primitives needed to simulate:

1. Environment constraints (Ω)
2. Revision mechanisms (C_rev)
3. Adaptive mechanism spaces (𝒢)
4. CTC-enabled vs closed adaptation
"""


from dataclasses import dataclass, field
from typing import Any, Dict, List


# ============================================================
# Environment Constraint
# ============================================================

@dataclass
class ConstraintSignal:
    """
    Represents extracted environmental information.

    Ω_t

    This is not raw sensory data.
    It represents structure relevant to adaptation.
    """

    source: str
    information: Dict[str, Any]
    strength: float = 1.0


# ============================================================
# Adaptive Mechanism Space
# ============================================================

@dataclass
class AdaptiveMechanismSpace:
    """
    Represents the reachable space of adaptive mechanisms.

    𝒢

    Examples:
        - search strategies
        - learning algorithms
        - representations
        - planning methods
    """

    mechanisms: List[str] = field(default_factory=list)

    def expand(self, new_mechanism: str):
        """
        Add a newly reachable adaptive mechanism.
        """

        if new_mechanism not in self.mechanisms:
            self.mechanisms.append(new_mechanism)

    def size(self) -> int:
        return len(self.mechanisms)


# ============================================================
# Revision Mechanism
# ============================================================

@dataclass
class RevisionMechanism:
    """
    C_rev

    Determines how the system changes its own adaptive process.

    Closed system:

        C_rev(t+1) = f(C_rev(t))

    CTC system:

        C_rev(t+1) = f(C_rev(t), E_t)
    """

    rules: Dict[str, Any] = field(default_factory=dict)

    def revise(self, constraint: ConstraintSignal | None = None):
        """
        Update revision rules.

        If constraint is None:
            internal-only modification

        If constraint exists:
            reality can influence revision
        """

        if constraint is None:
            self.rules["internal_update"] = True

        else:
            self.rules["environment_update"] = (
                constraint.source
            )


# ============================================================
# CTC Controller
# ============================================================

@dataclass
class CTCController:
    """
    Controls whether environmental constraints can modify
    adaptive mechanisms.

    CTC OFF:

        Ω_t ↛ Δ𝒢_(t+1)

    CTC ON:

        Ω_t → Δ𝒢_(t+1)
    """

    permeability_active: bool = False

    revision: RevisionMechanism = field(
        default_factory=RevisionMechanism
    )

    mechanism_space: AdaptiveMechanismSpace = field(
        default_factory=AdaptiveMechanismSpace
    )

    def apply_constraint(
        self,
        constraint: ConstraintSignal
    ):
        """
        Apply environmental influence.

        This is the central CTC operation.
        """

        if self.permeability_active:

            # Reality reaches C_rev
            self.revision.revise(constraint)

            # Reality can expand reachable mechanisms
            self._generate_mechanism(
                constraint
            )

        else:

            # Closed trajectory:
            # constraint affects state,
            # but not adaptive topology

            self.revision.revise(None)


    def _generate_mechanism(
        self,
        constraint: ConstraintSignal
    ):
        """
        Converts environmental structure into
        a possible adaptive mechanism.

        Simplified placeholder for future
        mechanism discovery algorithms.
        """

        mechanism = (
            f"adapt_to_{constraint.source}"
        )

        self.mechanism_space.expand(
            mechanism
        )


# ============================================================
# Agent Adaptive Loop
# ============================================================

@dataclass
class AdaptiveAgent:
    """
    Minimal adaptive agent.

    Tracks:

        X = state
        K = representation
        𝒢 = adaptive mechanism space
        C_rev = revision mechanism
    """

    controller: CTCController

    state: Dict[str, Any] = field(
        default_factory=dict
    )

    representation: Dict[str, Any] = field(
        default_factory=dict
    )


    def observe(
        self,
        environment_signal: ConstraintSignal
    ):
        """
        Receive environmental information.
        """

        self.representation.update(
            environment_signal.information
        )


    def adapt(
        self,
        constraint: ConstraintSignal
    ):
        """
        Perform adaptive update.
        """

        self.controller.apply_constraint(
            constraint
        )


# ============================================================
# Utility Functions
# ============================================================

def measure_permeability(
    agent: AdaptiveAgent
) -> float:
    """
    Simple proxy metric.

    Future versions should estimate:

        ∂C_rev / ∂E*

    or:

        Ω → Δ𝒢

    """

    if agent.controller.permeability_active:
        return 1.0

    return 0.0


def compare_mechanism_space(
    before: AdaptiveMechanismSpace,
    after: AdaptiveMechanismSpace
) -> int:
    """
    Measures:

        Δ𝒢

    """

    return (
        after.size()
        -
        before.size()
    )
