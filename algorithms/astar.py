"""Owner: Gaetano. A* prioritizes cost so far plus heuristic."""
from models import Graph, Heuristic, NodeId, SearchResult


def astar(graph: Graph, start: NodeId, goal: NodeId,
          heuristic: Heuristic) -> SearchResult:
    """TODO: best-cost updates, stale-entry checks, goal on pop, reconstruction.

    Do not mutate graph. Return shared metrics; invalid IDs raise ValueError.
    """
    raise NotImplementedError("Gaetano: implement A* search")
