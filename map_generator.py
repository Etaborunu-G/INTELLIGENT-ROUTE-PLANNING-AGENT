"""Owner: Member 2. Reproducible undirected road graphs."""
from models import Graph, MapConfig


def generate_map(config: MapConfig) -> Graph:
    """Generate using random.Random(config.seed).

    TODO: validate settings, generate unique coordinates and symmetric edges.
    Each edge costs Euclidean length times a multiplier >= 1.
    Raise ValueError for invalid settings. Disconnected maps are allowed.
    """
    raise NotImplementedError("Member 2: implement map generation")


def validate_graph(graph: Graph) -> None:
    """TODO: raise ValueError for invalid nodes, coordinates or road costs."""
    raise NotImplementedError("Member 2: implement graph validation")
