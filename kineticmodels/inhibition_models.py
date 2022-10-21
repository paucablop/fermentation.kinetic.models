from dataclasses import dataclass
from typing import Annotated
import numpy as np


@dataclass
class LinearInhibition:
    """
    Expression for the linear inhibition.
    """

    inhibition_constant: Annotated[float, "1 / gram / litre"]

    @classmethod
    def fromdict(cls, d: dict) -> "LinearInhibition":
        return cls(**d)

    def rate(self, inhibitor_concentration: Annotated[float, "gram / litre"]) -> float:
        return 1 - self.inhibition_constant * inhibitor_concentration

    def __parameters__(self) -> dict:
        return self.__annotations__


@dataclass
class ExponentialInhibition:
    """
    Expression for the exponential inhibition.
    """

    inhibition_constant: Annotated[float, "1 / gram / litre"]

    @classmethod
    def fromdict(cls, d: dict) -> "ExponentialInhibition":
        return cls(**d)

    def rate(self, inhibitor_concentration: Annotated[float, "gram / litre"]) -> float:
        return np.exp(-self.inhibition_constant * inhibitor_concentration)

    def __parameters__(self) -> dict:
        return self.__annotations__



@dataclass
class SuddenInhibition:
    """
    Expression for the sudden inhibition.
    """

    inhibition_constant: Annotated[float, "gram / litre"]

    @classmethod
    def fromdict(cls, d: dict) -> "SuddenInhibition":
        return cls(**d)

    def rate(self, inhibitor_concentration: Annotated[float, "gram / litre"]) -> float:
        return 1 - (self.inhibition_constant / inhibitor_concentration)

    def __parameters__(self) -> dict:
        return self.__annotations__

@dataclass
class InverseInhibition:
    """
    Expression for the inverse inhibition.
    """

    inhibition_constant: Annotated[float, "gram / litre"]

    @classmethod
    def fromdict(cls, d: dict) -> "InverseInhibition":
        return cls(**d)

    def rate(self, inhibitor_concentration: Annotated[float, "gram / litre"]) -> float:
        return 1 / (1 + self.inhibition_constant / inhibitor_concentration)

    def __parameters__(self) -> dict:
        return self.__annotations__