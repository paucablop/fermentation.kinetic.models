from dataclasses import dataclass
from typing import Annotated

@dataclass
class Monod:
    """
    Monod uptake model.
    """
    max_uptake_rate: Annotated[float, "1 / second"]
    affinity_constant: Annotated[float, "gram / litre"]

    @classmethod
    def fromdict(cls, d: dict) -> "Monod":
        return cls(**d)

    def rate(self, substrate_concentration:  Annotated[float, "gram / litre"]) -> float:
        return (
            self.max_uptake_rate
            * substrate_concentration
            / (self.affinity_constant + substrate_concentration)
        )

    def __parameters__(self) -> dict:
        return self.__annotations__


@dataclass
class MonodSubstrateInhibition:
    """
    Monod uptake model with substrate inhibition.
    """
    max_uptake_rate: Annotated[float, "1 / second"]
    affinity_constant: Annotated[float, "gram / litre"]
    substrate_inhibition_constant: Annotated[float, "grams/ litre"]

    @classmethod
    def fromdict(cls, d: dict) -> "MonodSubstrateInhibition":
        return cls(**d)

    def rate(self, substrate_concentration:  Annotated[float, "gram / litre"]) -> float:
        return (
            self.max_uptake_rate
            * substrate_concentration
            / (
                self.affinity_constant
                + substrate_concentration
                + (substrate_concentration**2) / self.substrate_inhibition_constant
            )
        )

    def __parameters__(self) -> dict:
        return self.__annotations__


@dataclass
class MonodSubstrateNonCompetitiveInhibition:
    """
    Monod uptake model with competitive substrate inhibition.
    """
    max_uptake_rate: Annotated[float, "1 / second"]
    affinity_constant: Annotated[float, "gram / litre"]
    substrate_inhibition_constant: Annotated[float, "gram / litre"]

    @classmethod
    def fromdict(cls, d: dict) -> "MonodSubstrateNonCompetitiveInhibition":
        return cls(**d)

    def rate(
        self,
        substrate_concentration:  Annotated[float, "gram / litre"],
    ) -> float:
        return self.max_uptake_rate / (
            (1.0 + self.affinity_constant / substrate_concentration)
            * (1.0 + substrate_concentration / self.substrate_inhibition_constant)
        )

    def __parameters__(self) -> dict:
        return self.__annotations__


@dataclass
class MonodSubstrateCompetitiveInhibition:
    """
    Monod uptake model with non-competitive substrate inhibition.
    """
    max_uptake_rate: Annotated[float, "1 / second"]
    affinity_constant: Annotated[float, "gram / litre"]
    substrate_inhibition_constant: Annotated[float, "gram / litre"]

    @classmethod
    def fromdict(cls, d: dict) -> "MonodSubstrateCompetitiveInhibition":
        return cls(**d)

    def rate(self, substrate_concentration: Annotated[float, "gram / litre"]) -> float:
        return (
            self.max_uptake_rate
            * substrate_concentration
            / (
                self.affinity_constant
                * (1.0 + substrate_concentration / self.substrate_inhibition_constant)
                + substrate_concentration
            )
        )

    def __parameters__(self) -> dict:
        return self.__annotations__