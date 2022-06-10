from dataclasses import dataclass


@dataclass
class Monod:
    """
    Monod uptake model.
    """

    max_uptake_rate: float
    affinity_constant: float

    @classmethod
    def fromdict(cls, d: dict) -> "Monod":
        return cls(**d)

    def calculate_rate(self, substrate_concentration: float) -> float:
        return (
            self.max_uptake_rate
            * substrate_concentration
            / (self.affinity_constant + substrate_concentration)
        )


@dataclass
class MonodSubstrateInhibition:
    """
    Monod uptake model with substrate inhibition.
    """

    max_uptake_rate: float
    affinity_constant: float
    inhibition_constant: float

    @classmethod
    def fromdict(cls, d: dict) -> "MonodSubstrateInhibition":
        return cls(**d)

    def calculate_rate(self, substrate_concentration: float) -> float:
        return (
            self.max_uptake_rate
            * substrate_concentration
            / (
                self.affinity_constant
                + substrate_concentration
                + (substrate_concentration**2) / self.inhibition_constant
            )
        )


@dataclass
class MonodSubstrateCompetitiveInhibition:
    """
    Monod uptake model with competitive substrate inhibition.
    """

    max_uptake_rate: float
    affinity_constant: float
    inhibition_constant: float

    @classmethod
    def fromdict(cls, d: dict) -> "MonodSubstrateCompetitiveInhibition":
        return cls(**d)

    def calculate_rate(
        self,
        substrate_concentration: float,
    ) -> float:
        return self.max_uptake_rate / (
            (1.0 + self.affinity_constant / substrate_concentration)
            * (1.0 + substrate_concentration / self.inhibition_constant)
        )


@dataclass
class MonodSubstrateNonCompetitiveInhibition:
    """
    Monod uptake model with non-competitive substrate inhibition.
    """

    max_uptake_rate: float
    affinity_constant: float
    inhibition_constant: float

    @classmethod
    def fromdict(cls, d: dict) -> "MonodSubstrateNonCompetitiveInhibition":
        return cls(**d)

    def calculate_rate(self, substrate_concentration: float) -> float:
        return (
            self.max_uptake_rate
            * substrate_concentration
            / (
                self.affinity_constant
                * (1.0 + substrate_concentration / self.inhibition_constant)
                + substrate_concentration
            )
        )
