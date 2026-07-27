"""
CTC Core Tests

These tests do not prove CTC is true.

They test whether the implementation
correctly represents the hypothesis:

    E* ⇝ C_rev

Core experimental questions:

1. Does environmental constraint information
   modify the revision mechanism?

2. Does increased permeability expand
   reachable adaptive mechanisms?

3. Does removing the causal pathway
   reduce long-term adaptation?

"""


import pytest


from src.environment import Environment

from src.ctc_core import (
    AdaptiveAgent,
    AdaptiveMechanismSpace
)

from src.simulator import (
    CTCSimulator,
    run_comparison
)



# ============================================================
# Mock Components
# ============================================================


class ClosedAgent(AdaptiveAgent):
    """
    Agent with:

        C_rev(t+1)=f(C_rev(t))

    Environment cannot modify
    its adaptive mechanism.
    """


    def adapt(self, omega):

        return self.result(
            capability=self.capability + 1,
            mechanisms=self.mechanisms
        )



class PermeableAgent(AdaptiveAgent):
    """
    Agent with:

        C_rev(t+1)=f(C_rev(t), E*)

    Environment can alter
    reachable mechanisms.
    """


    def adapt(self, omega):

        new_mechanisms = (
            self.mechanisms.expand(
                omega
            )
        )


        return self.result(
            capability=(
                self.capability + 1
                + omega
            ),
            mechanisms=new_mechanisms
        )



# ============================================================
# Test 1
# Environmental Access
# ============================================================


def test_environment_can_reach_revision_mechanism():

    environment = Environment(
        difficulty=10
    )


    closed = ClosedAgent()

    permeable = PermeableAgent()


    closed_result = (
        closed.adapt(
            environment.extract_constraints()
        )
    )


    permeable_result = (
        permeable.adapt(
            environment.extract_constraints()
        )
    )


    assert (
        permeable_result.mechanisms.size
        >=
        closed_result.mechanisms.size
    )



# ============================================================
# Test 2
# Mechanism Expansion
# ============================================================


def test_constraint_information_expands_generatable_space():

    mechanisms = (
        AdaptiveMechanismSpace()
    )


    initial_size = (
        mechanisms.size
    )


    omega = 5


    updated = (
        mechanisms.expand(
            omega
        )
    )


    assert (
        updated.size
        >
        initial_size
    )



# ============================================================
# Test 3
# Closed vs Permeable
# ============================================================


def test_permeability_improves_adaptation():

    environment = Environment(
        difficulty=10
    )


    closed_sim = CTCSimulator(
        environment,
        ClosedAgent()
    )


    permeable_sim = CTCSimulator(
        environment,
        PermeableAgent()
    )


    results = run_comparison(
        closed_sim,
        permeable_sim,
        steps=20
    )


    closed_score = (
        results["baseline"]
        .metrics[-1]
        .value
    )


    permeability_score = (
        results["permeability"]
        .metrics[-1]
        .value
    )


    assert (
        permeability_score
        >=
        closed_score
    )



# ============================================================
# Test 4
# Causal Cut
# ============================================================


def test_removing_permeability_breaks_ctc():

    environment = Environment(
        difficulty=10
    )


    agent = ClosedAgent()


    simulator = CTCSimulator(
        environment,
        agent
    )


    simulator.run(10)


    final_mechanisms = (
        simulator.state
        .mechanism_space
        .size
    )


    # Closed systems may improve capability,
    # but mechanism space should not expand
    # from environmental pressure.

    assert (
        final_mechanisms
        ==
        simulator.agent
        .mechanisms
        .size
    )



# ============================================================
# Test 5
# Core Hypothesis
# ============================================================


def test_core_hypothesis_omega_causes_delta_generator():

    environment = Environment(
        difficulty=20
    )


    agent = PermeableAgent()


    before = (
        agent.mechanisms.size
    )


    omega = (
        environment
        .extract_constraints()
    )


    agent.adapt(
        omega
    )


    after = (
        agent.mechanisms.size
    )


    assert (
        after
        >
        before
    )



# ============================================================
# Run directly
# ============================================================


if __name__ == "__main__":

    pytest.main()
