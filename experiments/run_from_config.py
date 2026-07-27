"""
CTC Config-Based Experiment Runner

Loads experiment parameters from YAML and runs
the Causal Permeability Principle benchmark.

Purpose:

Separate experimental design from execution.

The YAML file defines:

    - environment conditions
    - agent properties
    - permeability conditions
    - metrics
    - output settings

The runner executes the experiment.

Core hypothesis:

    Ω_t → Δ𝒢_(t+1)

where:

    Ω  = environmental constraint information

    Δ𝒢 = change in reachable adaptive mechanisms


Comparison:

Closed trajectory:

    C_rev,t+1 = f(C_rev,t)


Permeable lineage:

    C_rev,t+1 = f(C_rev,t,E*_t)

"""


from pathlib import Path
import yaml
import json


from experiments.run_ctc_benchmark import (
    run_trial,
    summarize_results
)



# ============================================================
# Configuration Loading
# ============================================================


def load_config(
    config_path
):
    """
    Load YAML experiment configuration.
    """


    with open(
        config_path,
        "r",
        encoding="utf-8"
    ) as file:

        return yaml.safe_load(file)



# ============================================================
# Experiment Execution
# ============================================================


def run_experiment(
    config
):
    """
    Execute benchmark using loaded parameters.
    """


    results = []


    trials = (
        config["simulation"]["trials"]
    )


    steps = (
        config["simulation"]
        ["steps_per_trial"]
    )


    difficulty_levels = (
        config["environment"]
        ["difficulty_levels"]
    )


    print(
        f"Running {trials} trials..."
    )


    for trial in range(trials):


        difficulty = (
            difficulty_levels[
                trial %
                len(difficulty_levels)
            ]
        )


        print(
            f"Trial {trial + 1}/{trials}"
            f" | difficulty={difficulty}"
        )


        result = run_trial(

            difficulty=difficulty,

            steps=steps

        )


        result["trial"] = trial


        results.append(
            result
        )


    return results



# ============================================================
# Save Experiment Output
# ============================================================


def save_output(
    config,
    results
):


    output_directory = Path(

        config["output"]
        ["directory"]

    )


    output_directory.mkdir(

        parents=True,

        exist_ok=True

    )


    summary = summarize_results(
        results
    )


    with open(

        output_directory /
        "results.json",

        "w",

        encoding="utf-8"

    ) as file:

        json.dump(

            results,

            file,

            indent=4

        )


    with open(

        output_directory /
        "summary.json",

        "w",

        encoding="utf-8"

    ) as file:

        json.dump(

            summary,

            file,

            indent=4

        )


    print(
        "\nResults saved:"
    )

    print(
        output_directory
    )


    return summary



# ============================================================
# Report
# ============================================================


def print_summary(
    summary
):


    print(
        "\n"
        "=" * 60
    )

    print(
        "CTC EXPERIMENT SUMMARY"
    )

    print(
        "=" * 60
    )


    for key, value in summary.items():

        print(
            f"{key}: {value}"
        )



# ============================================================
# Main
# ============================================================


if __name__ == "__main__":


    config_path = Path(

        "experiments/configs/default.yaml"

    )


    print(
        "Loading configuration:"
    )

    print(
        config_path
    )


    config = load_config(
        config_path
    )


    results = run_experiment(
        config
    )


    summary = save_output(

        config,

        results

    )


    print_summary(
        summary
    )


    print(
        "\nCTC benchmark complete."
    )
