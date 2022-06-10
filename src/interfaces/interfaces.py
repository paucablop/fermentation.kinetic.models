from dataclasses import dataclass


@dataclass
class IMonod:
    """Interface for monod uptake models."""

    max_uptake_rate: float
    affinity_constant: float

    def rate(self, substrate_concentration: float) -> float:
        """Calculate the rate of uptake."""
        pass


@dataclass
class IMonodInhibition(IMonod):
    """Interface for monod inhibition uptake models."""

    substrate_inhibition_constant: float
