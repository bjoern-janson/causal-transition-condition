"""
CTC Basic Experiment

Purpose:

Run the first minimal simulation comparing:

1. Closed trajectory

    C_rev,t+1 = f(C_rev,t)

    Reality affects outputs,
    but cannot modify the mechanism
    that creates future adaptations.


2. Permeable lineage

    C_rev,t+1 = f(C_rev,t, E*)

    Reality can modify the mechanism
    that determines future adaptation.

This experiment tests the core CTC hypothesis:

    Ω_t → Δ𝒢_(t+1)

where:

    Ω = constraint information from reality
    Δ𝒢 = change in reachable adaptive mechanisms


Expected result:

A permeable system should not necessarily
be stronger immediately.

Its advantage should appear as:

- larger reachable mechanism space
- better adaptation under changing environments
- increased residual capability after disruption
"""


from src.environment import Environment

from src.ctc_core import (
    AdaptiveAgent,
    ClosedAdaptiveAgent,
    PermeableAdaptiveAgent
)

from src.simulator import CTCSimulator

from src.metrics import (
    calculate_permeability_score,
    calculate_adaptation_score
)



def run_experiment():

    print("=" * 60)
    print("CTC BASIC EXPERIMENT")
    print("=" * 60)


    # --------------------------------------------------------
    # Create environment
    # --------------------------------------------------------

    environment = Environment(
        difficulty=10
    )


    print("\nEnvironment:")
    print(environment)



    # --------------------------------------------------------
    # Create agents
    # --------------------------------------------------------

    closed_agent = (
        ClosedAdaptiveAgent()
    )


    permeable_agent = (
        PermeableAdaptiveAgent()
    )


    print("\nAgents initialized:")
    print("- Closed trajectory")
    print("- Permeable lineage")



    # --------------------------------------------------------
    # Create simulators
    # --------------------------------------------------------

    closed_simulator = CTCSimulator(
        environment=environment,
        agent=closed_agent
    )


    permeable_simulator = CTCSimulator(
        environment=environment,
        agent=permeable_agent
    )



    # --------------------------------------------------------
    # Run simulations
    # --------------------------------------------------------

    steps = 50


    print(
        f"\nRunning {steps} adaptation cycles..."
    )


    closed_history = (
        closed_simulator.run(
            steps
        )
    )


    permeable_history = (
        permeable_simulator.run(
            steps
        )
    )



    # --------------------------------------------------------
    # Measure outcomes
    # --------------------------------------------------------

    closed_score = (
        calculate_adaptation_score(
            closed_history
        )
    )


    permeable_score = (
        calculate_adaptation_score(
            permeable_history
        )
    )


    closed_permeability = (
        calculate_permeability_score(
            closed_history
        )
    )


    permeable_permeability = (
        calculate_permeability_score(
            permeable_history
        )
    )



    # --------------------------------------------------------
    # Results
    # --------------------------------------------------------

    print("\nRESULTS")
    print("-" * 60)


    print(
        f"Closed adaptation score: "
        f"{closed_score:.3f}"
    )

    print(
        f"Permeable adaptation score: "
        f"{permeable_score:.3f}"
    )


    print()


    print(
        f"Closed permeability: "
        f"{closed_permeability:.3f}"
    )

    print(
        f"Permeable permeability: "
        f"{permeable_permeability:.3f}"
    )



    # --------------------------------------------------------
    # Core interpretation
    # --------------------------------------------------------

    print("\nINTERPRETATION")
    print("-" * 60)


    if (
        permeable_permeability
        >
        closed_permeability
    ):

        print(
            """
CTC prediction supported:

Environmental constraint information
successfully reached the adaptive
mechanism layer.

Observed:

E* → C_rev

The system preserved access between
reality and future possibility.
"""
        )

    else:

        print(
            """
CTC prediction not supported.

Reality did not produce measurable
changes in reachable adaptive mechanisms.
"""
        )



if __name__ == "__main__":

    run_experiment()
