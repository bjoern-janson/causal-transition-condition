"""
CTC Benchmark Runner

Purpose:

Run repeatable experiments comparing:

1. Closed trajectory systems

        C_rev,t+1 = f(C_rev,t)

2. Permeable lineage systems

        C_rev,t+1 = f(C_rev,t, E*)

The benchmark evaluates the CTC hypothesis:

        Ω_t → Δ𝒢_(t+1)

where:

    Ω  = environmental constraint information
    Δ𝒢 = expansion/change in reachable adaptive mechanisms


This file is not a proof of CTC.

It is an experimental protocol designed to test:

    Does environmental access to revision mechanisms
    produce measurable differences in adaptation?
"""


from pathlib import Path
import json
import random


from src.environment import Environment

from src.ctc_core import (
    ClosedAdaptiveAgent,
    PermeableAdaptiveAgent
)

from src.simulator import CTCSimulator

from src.metrics import (
    calculate_adaptation_score,
    calculate_permeability_score
)



# ============================================================
# Configuration
# ============================================================


DEFAULT_CONFIG = {

    "trials": 20,

    "steps": 100,

    "environment_difficulty": [
        1,
        5,
        10,
        20,
        50
    ],

    "output_directory":
        "results/benchmark"

}



# ============================================================
# Single Trial
# ============================================================


def run_trial(
    difficulty: int,
    steps: int
):
    """
    Run one closed vs permeable comparison.
    """


    environment = Environment(
        difficulty=difficulty
    )


    closed_agent = (
        ClosedAdaptiveAgent()
    )


    permeable_agent = (
        PermeableAdaptiveAgent()
    )


    closed_simulator = CTCSimulator(
        environment,
        closed_agent
    )


    permeable_simulator = CTCSimulator(
        environment,
        permeable_agent
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


    return {

        "difficulty": difficulty,

        "closed": {

            "adaptation":
                calculate_adaptation_score(
                    closed_history
                ),

            "permeability":
                calculate_permeability_score(
                    closed_history
                )

        },


        "permeable": {

            "adaptation":
                calculate_adaptation_score(
                    permeable_history
                ),

            "permeability":
                calculate_permeability_score(
                    permeable_history
                )

        }

    }



# ============================================================
# Full Benchmark
# ============================================================


def run_benchmark(
    config=DEFAULT_CONFIG
):
    """
    Run complete benchmark suite.
    """


    results = []


    for trial in range(
        config["trials"]
    ):


        difficulty = random.choice(
            config[
                "environment_difficulty"
            ]
        )


        print(
            f"Trial {trial + 1}/"
            f"{config['trials']} "
            f"| difficulty={difficulty}"
        )


        result = run_trial(

            difficulty=difficulty,

            steps=config["steps"]

        )


        result["trial"] = trial


        results.append(
            result
        )


    return results



# ============================================================
# Summary Statistics
# ============================================================


def summarize_results(
    results
):
    """
    Aggregate benchmark outcomes.
    """


    closed_scores = []

    permeable_scores = []


    for result in results:

        closed_scores.append(

            result["closed"]
            ["adaptation"]

        )


        permeable_scores.append(

            result["permeable"]
            ["adaptation"]

        )


    summary = {


        "trials":

            len(results),


        "average_closed":

            sum(closed_scores)
            /
            len(closed_scores),


        "average_permeable":

            sum(permeable_scores)
            /
            len(permeable_scores),


        "improvement":

            (
                sum(permeable_scores)
                /
                len(permeable_scores)
            )
            -
            (
                sum(closed_scores)
                /
                len(closed_scores)
            )

    }


    return summary



# ============================================================
# Save Results
# ============================================================


def save_results(
    results,
    summary,
    directory
):


    path = Path(directory)

    path.mkdir(
        parents=True,
        exist_ok=True
    )


    with open(
        path / "benchmark_results.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            results,
            file,
            indent=4
        )


    with open(
        path / "benchmark_summary.json",
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            summary,
            file,
            indent=4
        )



# ============================================================
# Main
# ============================================================


if __name__ == "__main__":


    print(
        "=" * 60
    )

    print(
        "CTC PERMEABILITY BENCHMARK"
    )

    print(
        "=" * 60
    )


    results = run_benchmark()


    summary = summarize_results(
        results
    )


    save_results(

        results,

        summary,

        DEFAULT_CONFIG[
            "output_directory"
        ]

    )


    print("\nSUMMARY")
    print("-" * 60)


    for key, value in summary.items():

        print(
            f"{key}: {value}"
        )


    print(
        "\nBenchmark complete."
    )
