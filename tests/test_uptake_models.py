import kineticmodels as km
import pytest


def test_monod_rate():
    # Arrange
    substrate_concentration = 0.5
    max_uptake_rate = 1
    affinity_constant = 0.5

    # Act
    kinetics = km.Monod(max_uptake_rate, affinity_constant)
    rate = kinetics.rate(substrate_concentration)

    # Assert
    assert pytest.approx(rate, 1e-8) == 0.5


def test_monod_rate_from_dict():
    # Arrange
    substrate_concentration = 0.5
    parameters = {
        "max_uptake_rate": 1,
        "affinity_constant": 0.5,
    }

    # Act
    kinetics = km.Monod.fromdict(parameters)
    rate = kinetics.rate(substrate_concentration)

    # Assert
    assert pytest.approx(rate, 1e-8) == 0.5


def test_monod_substrate_inhibition_rate():
    # Arrange
    substrate_concentration = 1.0
    max_uptake_rate = 0.5
    affinity_constant = 0.5
    substrate_inhibition_constant = 1.0

    # Act
    kinetics = km.MonodSubstrateInhibition(
        max_uptake_rate,
        affinity_constant,
        substrate_inhibition_constant,
    )
    rate = kinetics.rate(substrate_concentration)

    # Assert
    assert pytest.approx(rate, 1e-8) == 0.2


def test_monod_substrate_inhibition_rate_from_dict():
    # Arrange
    substrate_concentration = 1.0
    parameters = {
        "max_uptake_rate": 0.5,
        "affinity_constant": 0.5,
        "substrate_inhibition_constant": 1.0,
    }

    # Act
    kinetics = km.MonodSubstrateInhibition.fromdict(parameters)
    rate = kinetics.rate(substrate_concentration)

    # Assert
    assert pytest.approx(rate, 1e-8) == 0.2


def test_monod_substrate_competitive_inhibition_rate():
    # Arrange
    substrate_concentration = 0.5
    max_uptake_rate = 1.0
    affinity_constant = 0.5
    substrate_inhibition_constant = 1.0

    # Act
    kinetics = km.MonodSubstrateCompetitiveInhibition(
        max_uptake_rate,
        affinity_constant,
        substrate_inhibition_constant,
    )
    rate = kinetics.rate(substrate_concentration=substrate_concentration)

    # Assert
    assert pytest.approx(rate, 1e-8) == 0.3333333333333333


def test_monod_substrate_competitive_inhibition_rate_fom_dict():
    # Arrange
    substrate_concentration = 0.5
    parameters = {
        "max_uptake_rate": 1.0,
        "affinity_constant": 0.5,
        "substrate_inhibition_constant": 1.0,
    }

    # Act
    kinetics = km.MonodSubstrateCompetitiveInhibition.fromdict(parameters)
    rate = kinetics.rate(substrate_concentration=substrate_concentration)

    # Assert
    assert pytest.approx(rate, 1e-8) == 0.3333333333333333


def test_monod_substrate_non_competitive_inhibition_rate():
    # Arrange
    substrate_concentration = 0.5
    max_uptake_rate = 1.0
    affinity_constant = 0.5
    substrate_inhibition_constant = 1.0

    # Act
    kinetics = km.MonodSubstrateNonCompetitiveInhibition(
        max_uptake_rate=max_uptake_rate,
        affinity_constant=affinity_constant,
        substrate_inhibition_constant=substrate_inhibition_constant,
    )
    rate = kinetics.rate(substrate_concentration)
    # Assert
    assert pytest.approx(rate, 1e-8) == 0.4


def test_monod_substrate_non_competitive_inhibition_rate_dict():
    # Arrange
    substrate_concentration = 0.5
    parameters = {
        "max_uptake_rate": 1.0,
        "affinity_constant": 0.5,
        "substrate_inhibition_constant": 1.0,
    }

    # Act
    kinetics = km.MonodSubstrateNonCompetitiveInhibition.fromdict(parameters)
    rate = kinetics.rate(substrate_concentration)
    # Assert
    assert pytest.approx(rate, 1e-8) == 0.4
