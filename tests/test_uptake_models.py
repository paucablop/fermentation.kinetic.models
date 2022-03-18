from src.kineticmodels.uptake_models import Monod
from src.kineticmodels.uptake_models import MonodSubstrateInhibition
from src.kineticmodels.uptake_models import MonodSubstrateCompetitiveInhibition
from src.kineticmodels.uptake_models import MonodSubstrateNonCompetitiveInhibition

import pytest


def test_monod_rate():
    # Arrange
    substrate_concentration = 0.5
    max_growth_rate = 1
    affinity_constant = 0.5

    # Act
    rate = Monod.rate(substrate_concentration, max_growth_rate, affinity_constant)

    # Assert
    assert pytest.approx(rate, 1e-8) == 0.5

def test_monod_substrate_inhibition_rate():
    # Arrange
    substrate_concentration = 1.0
    max_growth_rate = 0.5
    affinity_constant = 0.5
    substrate_inhibition_constant = 1.0

    # Act
    rate = MonodSubstrateInhibition.rate(substrate_concentration, max_growth_rate, affinity_constant, substrate_inhibition_constant)

    # Assert
    assert pytest.approx(rate, 1e-8) == 0.2


def test_monod_substrate_competitive_inhibition_rate():
    # Arrange
    substrate_concentration = 0.5
    max_growth_rate = 1.0
    affinity_constant = 0.5
    substrate_inhibition_constant = 1.0

    # Act
    rate = MonodSubstrateCompetitiveInhibition.rate(substrate_concentration, max_growth_rate, affinity_constant, substrate_inhibition_constant)

    # Assert
    assert pytest.approx(rate, 1e-8) == 0.3333333333333333



def test_monod_substrate_non_competitive_inhibition_rate():
    # Arrange
    substrate_concentration = 0.5
    max_growth_rate = 1.0
    affinity_constant = 0.5
    substrate_inhibition_constant = 1.0

    # Act
    rate = MonodSubstrateNonCompetitiveInhibition.rate(substrate_concentration, max_growth_rate, affinity_constant, substrate_inhibition_constant)

    # Assert
    assert pytest.approx(rate, 1e-8) == 0.4
