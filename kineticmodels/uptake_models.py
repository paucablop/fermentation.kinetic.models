from kineticmodels.interfaces import IMonod, IMonodInhibition


class Monod(IMonod):
    """
    Monod uptake model.
    """

    @classmethod
    def fromdict(cls, d: dict) -> "Monod":
        return cls(**d)

    def rate(self, substrate_concentration: float) -> float:
        return (
            self.max_uptake_rate
            * substrate_concentration
            / (self.affinity_constant + substrate_concentration)
        )


class MonodSubstrateInhibition(IMonodInhibition):
    """
    Monod uptake model with substrate inhibition.
    """

    @classmethod
    def fromdict(cls, d: dict) -> "MonodSubstrateInhibition":
        return cls(**d)

    def rate(self, substrate_concentration: float) -> float:
        return (
            self.max_uptake_rate
            * substrate_concentration
            / (
                self.affinity_constant
                + substrate_concentration
                + (substrate_concentration**2) / self.substrate_inhibition_constant
            )
        )


class MonodSubstrateCompetitiveInhibition(IMonodInhibition):
    """
    Monod uptake model with competitive substrate inhibition.
    """

    @classmethod
    def fromdict(cls, d: dict) -> "MonodSubstrateCompetitiveInhibition":
        return cls(**d)

    def rate(
        self,
        substrate_concentration: float,
    ) -> float:
        return self.max_uptake_rate / (
            (1.0 + self.affinity_constant / substrate_concentration)
            * (1.0 + substrate_concentration / self.substrate_inhibition_constant)
        )


class MonodSubstrateNonCompetitiveInhibition(IMonodInhibition):
    """
    Monod uptake model with non-competitive substrate inhibition.
    """

    @classmethod
    def fromdict(cls, d: dict) -> "MonodSubstrateNonCompetitiveInhibition":
        return cls(**d)

    def rate(self, substrate_concentration: float) -> float:
        return (
            self.max_uptake_rate
            * substrate_concentration
            / (
                self.affinity_constant
                * (1.0 + substrate_concentration / self.substrate_inhibition_constant)
                + substrate_concentration
            )
        )
