"""Owner: Gaetano. Heuristics receive graph, current node and goal."""
from models import Graph, NodeId


def euclidean_distance(graph: Graph, node: NodeId, goal: NodeId) -> float:
    """TODO: straight-line distance using graph.positions.

    The graph cost rule makes this admissible and consistent.
    """
    raise NotImplementedError("Gaetano: implement Euclidean heuristic")


def zero_heuristic(graph: Graph, node: NodeId, goal: NodeId) -> float:
    """A* with this heuristic uses UCS priorities."""
    return 0.0
