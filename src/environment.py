"""
CTC Environment

Defines the external world used by the simulator.

The environment is responsible for generating:

    E_t

and extracting:

    Ω_t

where:

    E_t = full environmental state
    Ω_t = constraint information relevant to adaptation

The CTC hypothesis depends on whether Ω_t can influence:

    C_rev

and therefore:

    Δ𝒢
"""


from dataclasses import dataclass, field
from typing import Any, Dict, List


from .ctc_core import ConstraintSignal


# ============================================================
# Environment State
# ============================================================

@dataclass
class EnvironmentState:
    """
    Represents the current world state.

    E_t
    """

    task: str

    rules: Dict[str, Any]

    difficulty: float = 1.0

    timestep: int = 0


# ============================================================
# Environment
# ============================================================

@dataclass
class Environment:
    """
    Base environment.

    Generates changing conditions that test
    adaptive systems.

    The environment does not directly modify
    the agent.

    It only produces constraints.
    """

    state: EnvironmentState

    history: List[EnvironmentState] = field(
        default_factory=list
    )


    def step(self):
        """
        Advance environment time.
        """

        self.history.append(
            self.state
        )

        self.state.timestep += 1


    def observe(self) -> Dict[str, Any]:
        """
        Return observable information.

        This represents what an agent can perceive.
        """

        return {
            "task": self.state.task,
            "difficulty": self.state.difficulty,
            "rules": self.state.rules
        }


    def extract_constraints(self) -> ConstraintSignal:
        """
        Convert environmental state into Ω_t.

        This is the key abstraction.

        Raw reality:

            E_t

        becomes usable constraint information:

            Ω_t
        """

        return ConstraintSignal(
            source=self.state.task,
            information={
                "rules": self.state.rules,
                "difficulty": self.state.difficulty,
            },
            strength=1.0
        )


# ============================================================
# Environment Perturbations
# ============================================================

class EnvironmentPerturbation:
    """
    Generates changes in reality.

    Represents:

        ΔE

    Examples:

        - rule changes
        - new constraints
        - changed objectives
    """


    @staticmethod
    def change_rule(
        environment: Environment,
        key: str,
        value: Any
    ):
        """
        Modify an environmental rule.
        """

        environment.state.rules[key] = value


    @staticmethod
    def increase_difficulty(
        environment: Environment,
        amount: float
    ):
        """
        Increase environmental pressure.
        """

        environment.state.difficulty += amount


    @staticmethod
    def change_task(
        environment: Environment,
        new_task: str
    ):
        """
        Change the objective itself.

        Tests whether the system can
        adapt beyond its previous assumptions.
        """

        environment.state.task = new_task


# ============================================================
# Benchmark Environments
# ============================================================

def create_simple_environment():
    """
    Minimal test environment.

    Used for first CTC experiments.
    """

    return Environment(
        state=EnvironmentState(
            task="navigation",
            rules={
                "movement": "grid",
                "goal": "reach_target"
            },
            difficulty=1.0
        )
    )


def create_rule_shift_environment():
    """
    Environment designed to test
    adaptation under changing rules.
    """

    return Environment(
        state=EnvironmentState(
            task="strategy_game",
            rules={
                "reward": "maximize_score",
                "movement": "standard"
            },
            difficulty=1.0
        )
    )


def create_open_ended_environment():
    """
    Environment designed to test
    whether agents can discover
    new adaptive mechanisms.

    Future versions should include:

        - hidden variables
        - changing objectives
        - generated tasks
    """

    return Environment(
        state=EnvironmentState(
            task="open_problem",
            rules={
                "objective": "discover_solution"
            },
            difficulty=1.0
        )
    )
