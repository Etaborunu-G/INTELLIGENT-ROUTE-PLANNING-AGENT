"""Owner: Gaetano. Shared dispatcher for the UI and experiments."""
from algorithms.astar import astar
from algorithms.greedy import greedy
from algorithms.ucs import ucs
from heuristics import euclidean_distance, zero_heuristic
from models import Graph, NodeId, SearchResult


def run_search(graph: Graph, start: NodeId, goal: NodeId,
               algorithm: str, heuristic: str = "euclidean") -> SearchResult:
    """Select an implementation. UCS ignores the heuristic setting."""
    if algorithm not in {"ucs", "greedy", "astar"}:
        raise ValueError(f"Unknown algorithm: {algorithm}")
    if start not in graph.positions or goal not in graph.positions:
        raise ValueError("Start and goal must exist in the graph")
    if algorithm == "ucs":
        return ucs(graph, start, goal)
    heuristics = {"euclidean": euclidean_distance, "zero": zero_heuristic}
    if heuristic not in heuristics:
        raise ValueError(f"Unknown heuristic: {heuristic}")
    implementation = greedy if algorithm == "greedy" else astar
    return implementation(graph, start, goal, heuristics[heuristic])
