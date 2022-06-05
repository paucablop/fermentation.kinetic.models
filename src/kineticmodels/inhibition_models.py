class Monod:
    def __init__(self, max_uptake_rate: float, affinity_constant: float) -> None:
        self.max_uptake_rate = max_uptake_rate
        self.affinity_constant = affinity_constant

    def calculate_rate(self, substrate_concentration: float) -> float:
        return (
            self.max_uptake_rate
            * substrate_concentration
            / (self.affinity_constant + substrate_concentration)
        )


class MonodSubstrateInhibition:
    def __init__(
        self,
        max_uptake_rate: float,
        affinity_constant: float,
        inhibition_constant: float,
    ) -> None:
        self.max_uptake_rate = max_uptake_rate
        self.affinity_constant = affinity_constant
        self.inhibition_constant = inhibition_constant

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


class MonodSubstrateCompetitiveInhibition:
    def __init__(
        self,
        max_uptake_rate: float,
        affinity_constant: float,
        inhibition_constant: float,
    ) -> None:
        self.max_uptake_rate = max_uptake_rate
        self.affinity_constant = affinity_constant
        self.inhibition_constant = inhibition_constant

    def calculate_rate(
        self,
        substrate_concentration: float,
    ) -> float:
        return self.max_uptake_rate / (
            (1.0 + self.affinity_constant / substrate_concentration)
            * (1.0 + substrate_concentration / self.inhibition_constant)
        )


class MonodSubstrateNonCompetitiveInhibition:
    def __init__(
        self,
        max_uptake_rate: float,
        affinity_constant: float,
        inhibition_constant: float,
    ) -> None:
        self.max_uptake_rate = max_uptake_rate
        self.affinity_constant = affinity_constant
        self.inhibition_constant = inhibition_constant

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
