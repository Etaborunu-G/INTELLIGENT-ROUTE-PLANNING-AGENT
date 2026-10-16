"""Owner: Member 4. Greedy prioritizes estimated remaining cost."""
from models import Graph, Heuristic, NodeId, SearchResult


def greedy(graph: Graph, start: NodeId, goal: NodeId,
           heuristic: Heuristic) -> SearchResult:
    """TODO: heuristic frontier, first-discovery tracking and reconstruction.

    Returned paths must be valid but need not have minimum cost.
    """
    raise NotImplementedError("Member 4: implement Greedy Best-First Search")
