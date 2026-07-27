"""
CTC Export Results

Exports experiment outputs into portable formats.

Purpose:

- preserve experiment runs
- enable comparison between agents
- allow external analysis
- create reproducible research artifacts

Supported formats:

    JSON
    CSV

The exported data should contain:

    timestep
    capability
    mechanism expansion
    environment constraints
    permeability metrics
"""


import json
import csv
from pathlib import Path
from typing import List, Dict



# ============================================================
# JSON Export
# ============================================================


def export_json(
    results: Dict,
    filepath: str
):
    """
    Export complete experiment results.

    Example:

        export_json(
            results,
            "results/run_001.json"
        )

    """

    path = Path(filepath)

    path.parent.mkdir(
        parents=True,
        exist_ok=True
    )


    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            results,
            file,
            indent=4
        )



# ============================================================
# CSV Export
# ============================================================


def export_history_csv(
    history: List[Dict],
    filepath: str
):
    """
    Export timestep history.

    Expected format:

    [
        {
            "timestep": 1,
            "capability": 0.5,
            "mechanism_expansion": 2
        }
    ]

    """


    path = Path(filepath)

    path.parent.mkdir(
        parents=True,
        exist_ok=True
    )


    if not history:
        return


    keys = list(
        history[0].keys()
    )


    with open(
        path,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=keys
        )

        writer.writeheader()

        writer.writerows(
            history
        )



# ============================================================
# Experiment Bundle Export
# ============================================================


def export_experiment(
    experiment_name: str,
    closed_history: List[Dict],
    permeable_history: List[Dict],
    metrics: Dict,
    output_dir: str = "results"
):
    """
    Save a complete CTC experiment.

    Structure:

    results/
        experiment_name/
            metadata.json
            closed_history.csv
            permeable_history.csv

    """


    directory = Path(output_dir) / experiment_name


    directory.mkdir(
        parents=True,
        exist_ok=True
    )


    metadata = {
        "experiment": experiment_name,

        "hypothesis":
            "Ω_t → Δ𝒢_(t+1)",

        "definition":
            "Environmental constraint information "
            "changes reachable adaptive mechanisms",

        "metrics":
            metrics
    }


    export_json(
        metadata,
        directory / "metadata.json"
    )


    export_history_csv(
        closed_history,
        directory / "closed_history.csv"
    )


    export_history_csv(
        permeable_history,
        directory / "permeable_history.csv"
    )


# ============================================================
# Example Usage
# ============================================================


if __name__ == "__main__":


    example_closed = [

        {
            "timestep": 0,
            "capability": 0.1,
            "mechanism_expansion": 0
        },

        {
            "timestep": 1,
            "capability": 0.2,
            "mechanism_expansion": 0
        }

    ]


    example_permeable = [

        {
            "timestep": 0,
            "capability": 0.1,
            "mechanism_expansion": 0
        },

        {
            "timestep": 1,
            "capability": 0.3,
            "mechanism_expansion": 1
        }

    ]


    example_metrics = {

        "permeability_score": 0.95,

        "mechanism_growth": 1.0,

        "residual_capability": 0.85

    }


    export_experiment(

        experiment_name="first_ctc_run",

        closed_history=example_closed,

        permeable_history=example_permeable,

        metrics=example_metrics

    )


    print(
        "CTC experiment exported."
    )
