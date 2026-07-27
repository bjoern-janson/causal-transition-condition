"""
CTC Simulator

Connects:

    Environment
        ↓
        Ω_t (constraint information)
        ↓
    CTC Controller
        ↓
        C_rev update
        ↓
        𝒢 expansion
        ↓
    Metrics

The simulator compares:

1. Standard adaptation
    Environment affects outputs

2. CTC adaptation
    Environment affects the mechanism
    that generates future adaptations

The core experimental question:

    Does Ω_t → Δ𝒢_(t+1)
    
produce better long-term adaptation than
ordinary optimization?
"""


from dataclasses import dataclass, field
from typing import List, Dict


from .environment import Environment
from .ctc_core import (
    AdaptiveAgent,
    AdaptiveMechanismSpace
)

from .metrics import (
    mechanism_expansion,
    adaptation_velocity,
    permeability_score,
    residual_capability,
    dependency_score,
    ctc_score,
    MetricResult
)



# ============================================================
# Simulation State
# ============================================================


@dataclass
class SimulationState:
    """
    Tracks the state of an experiment.

    """

    timestep: int = 0

    capability: float = 0.0

    mechanism_space: AdaptiveMechanismSpace = field(
        default_factory=AdaptiveMechanismSpace
    )

    history: List[Dict] = field(
        default_factory=list
    )



# ============================================================
# CTC Simulator
# ============================================================


class CTCSimulator:
    """
    Main experiment engine.

    Runs an adaptive system through
    changing environments.
    """


    def __init__(
        self,
        environment: Environment,
        agent: AdaptiveAgent
    ):

        self.environment = environment

        self.agent = agent

        self.state = SimulationState()



    # --------------------------------------------------------
    # One timestep
    # --------------------------------------------------------

    def step(self):
        """
        Execute one adaptive cycle.

        """

        previous_mechanisms = (
            self.state.mechanism_space
        )


        # Reality generates constraints

        omega = (
            self.environment
            .extract_constraints()
        )


        # Agent updates

        result = (
            self.agent.adapt(
                omega
            )
        )


        # Environment advances

        self.environment.step()


        # Track new state

        self.state.timestep += 1


        self.state.capability = (
            result.capability
        )


        self.state.mechanism_space = (
            result.mechanisms
        )


        expansion = mechanism_expansion(
            previous_mechanisms,
            result.mechanisms
        )


        self.state.history.append(
            {
                "timestep":
                    self.state.timestep,

                "capability":
                    self.state.capability,

                "mechanism_expansion":
                    expansion.value
            }
        )


        return result



    # --------------------------------------------------------
    # Run experiment
    # --------------------------------------------------------

    def run(
        self,
        steps: int
    ):

        results = []


        for _ in range(steps):

            results.append(
                self.step()
            )


        return results



# ============================================================
# Benchmark Comparison
# ============================================================


@dataclass
class BenchmarkResult:

    name: str

    metrics: List[MetricResult]



def evaluate_agent(
    simulator: CTCSimulator
) -> BenchmarkResult:
    """
    Evaluate a completed run.

    """

    permeability = (
        permeability_score(
            simulator.agent
        )
    )


    history = simulator.state.history


    if len(history) > 1:

        growth = (
            history[-1]
            ["mechanism_expansion"]
        )

    else:

        growth = 0



    residual = residual_capability(
        before_removal=(
            simulator.state.capability
        ),
        after_removal=(
            simulator.state.capability * 0.5
        )
    )


    dependency = dependency_score(
        external_capability=0.5,
        independent_capability=0.5
    )


    composite = ctc_score(
        permeability.value,
        growth,
        residual.value,
        dependency.value
    )


    return BenchmarkResult(
        name="CTC Evaluation",
        metrics=[
            permeability,
            residual,
            dependency,
            composite
        ]
    )



# ============================================================
# Experiment Helpers
# ============================================================


def run_comparison(
    baseline: CTCSimulator,
    permeability_mode: CTCSimulator,
    steps: int = 100
):
    """
    Compare:

        Standard mode
        vs
        CTC permeability mode

    """

    baseline.run(steps)

    permeability_mode.run(steps)


    return {
        "baseline":
            evaluate_agent(
                baseline
            ),

        "permeability":
            evaluate_agent(
                permeability_mode
            )
    }



# ============================================================
# Simple Experiment
# ============================================================


def run_first_experiment(
    baseline_agent,
    ctc_agent,
    environment
):
    """
    First minimal CTC experiment.

    Tests:

        Does reality-linked
        revision improve adaptation?

    """

    baseline = CTCSimulator(
        environment=environment,
        agent=baseline_agent
    )


    permeability = CTCSimulator(
        environment=environment,
        agent=ctc_agent
    )


    return run_comparison(
        baseline,
        permeability
    )
