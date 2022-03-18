import numpy as np


class Monod:
    def rate(
        substrate_concentration: float, max_uptake_rate: float, affinity_constant: float
    ) -> float:
        return (
            max_uptake_rate
            * substrate_concentration
            / (affinity_constant + substrate_concentration)
        )


class MonodSubstrateInhibition:
    def rate(
        substrate_concentration: float,
        max_uptake_rate: float,
        affinity_constant: float,
        inhibition_constant: float,
    ) -> float:
        return (
            max_uptake_rate
            * substrate_concentration
            / (
                affinity_constant
                + substrate_concentration
                + (substrate_concentration**2) / inhibition_constant
            )
        )


class MonodSubstrateCompetitiveInhibition:
    def rate(
        substrate_concentration: float,
        max_uptake_rate: float,
        affinity_constant: float,
        inhibition_constant: float,
    ) -> float:
        return max_uptake_rate / (
            (1.0 + affinity_constant / substrate_concentration)
            * (1.0 + substrate_concentration / inhibition_constant)
        )


class MonodSubstrateNonCompetitiveInhibition:
    def rate(
        substrate_concentration: float,
        max_uptake_rate: float,
        affinity_constant: float,
        inhibition_constant: float,
    ) -> float:
        return (
            max_uptake_rate
            * substrate_concentration
            / (
                affinity_constant
                * (1.0 + substrate_concentration / inhibition_constant)
                + substrate_concentration
            )
        )
