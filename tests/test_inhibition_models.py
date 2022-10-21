import kineticmodels as km
import pytest


def test_linear_inhibiton():
    # Arrange
    inhibitor_concentration = 0.5
    inhibition_constant = 0.5

    # Act
    inhibition = km.LinearInhibition(inhibition_constant)
    rate = inhibition.rate(inhibitor_concentration)

    # Assert
    assert pytest.approx(rate, 1e-8) == 0.75


def test_linear_inhibiton_from_dict():
    # Arrange
    inhibitor_concentration = 0.5
    parameters = {
        "inhibition_constant": 0.5,
    }

    # Act
    inhibition = km.LinearInhibition.fromdict(parameters)
    rate = inhibition.rate(inhibitor_concentration)

    # Assert
    assert pytest.approx(rate, 1e-8) == 0.75


def test_exponential_inhibiton():
    # Arrange
    inhibitor_concentration = 0.5
    inhibition_constant = 0.5

    # Act
    inhibition = km.ExponentialInhibition(inhibition_constant)
    rate = inhibition.rate(inhibitor_concentration)

    # Assert
    assert pytest.approx(rate, 1e-8) == 0.7788007830714049


def test_exponential_inhibiton_from_dict():
    # Arrange
    inhibitor_concentration = 0.5
    parameters = {
        "inhibition_constant": 0.5,
    }

    # Act
    inhibition = km.ExponentialInhibition.fromdict(parameters)
    rate = inhibition.rate(inhibitor_concentration)

    # Assert
    assert pytest.approx(rate, 1e-8) == 0.7788007830714049


def test_sudden_inhibiton():
    # Arrange
    inhibitor_concentration = 0.5
    inhibition_constant = 0.5

    # Act
    inhibition = km.SuddenInhibition(inhibition_constant)
    rate = inhibition.rate(inhibitor_concentration)

    # Assert
    assert pytest.approx(rate, 1e-8) == 0.0


def test_sudden_inhibiton_from_dict():
    # Arrange
    inhibitor_concentration = 0.5
    parameters = {
        "inhibition_constant": 0.5,
    }

    # Act
    inhibition = km.SuddenInhibition.fromdict(parameters)
    rate = inhibition.rate(inhibitor_concentration)

    # Assert
    assert pytest.approx(rate, 1e-8) == 0.0


def test_inverse_inhibition():
    # Arrange
    inhibitor_concentration = 0.5
    inhibition_constant = 0.5

    # Act
    inhibition = km.InverseInhibition(inhibition_constant)
    rate = inhibition.rate(inhibitor_concentration)

    # Assert
    assert pytest.approx(rate, 1e-8) == 0.5


def test_inverse_inhibition_from_dict():
    # Arrange
    inhibitor_concentration = 0.5
    parameters = {
        "inhibition_constant": 0.5,
    }

    # Act
    inhibition = km.InverseInhibition.fromdict(parameters)
    rate = inhibition.rate(inhibitor_concentration)

    # Assert
    assert pytest.approx(rate, 1e-8) == 0.5


def test_parmeters_annotations():
    # Arrange
    inhibition_constant = 0.5

    # Act
    linear_inhibition = km.LinearInhibition(inhibition_constant)
    exponential_inhibition = km.ExponentialInhibition(inhibition_constant)
    sudden_inhibition = km.SuddenInhibition(inhibition_constant)
    inverse_inhibition = km.InverseInhibition(inhibition_constant)

    # Assert
    assert type(linear_inhibition.__parameters__()) is dict
    assert type(exponential_inhibition.__parameters__()) is dict
    assert type(sudden_inhibition.__parameters__()) is dict
    assert type(inverse_inhibition.__parameters__()) is dict


def test_parmeters_annotations_from_dict():
    # Arrange
    parameters = {
        "inhibition_constant": 0.5,
    }

    # Act
    linear_inhibition = km.LinearInhibition.fromdict(parameters)
    exponential_inhibition = km.ExponentialInhibition.fromdict(parameters)
    sudden_inhibition = km.SuddenInhibition.fromdict(parameters)
    inverse_inhibition = km.InverseInhibition.fromdict(parameters)

    # Assert
    assert type(linear_inhibition.__parameters__()) is dict
    assert type(exponential_inhibition.__parameters__()) is dict
    assert type(sudden_inhibition.__parameters__()) is dict
    assert type(inverse_inhibition.__parameters__()) is dict
