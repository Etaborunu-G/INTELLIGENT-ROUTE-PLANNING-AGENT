"""Gaetano: A* and the shared straight-line heuristic."""


def straight_line_distance(graph, node, goal):
    """TODO: calculate distance using graph["positions"]."""
    raise NotImplementedError("Gaetano: implement straight-line distance")


def astar(graph, start, goal, use_heuristic=True):
    """Return the result dictionary described in README.md.

    TODO: prioritize cost so far plus straight-line distance. When
    use_heuristic=False, use zero for the estimate to compare against UCS.
    Update better costs/parents, skip stale entries and check goal on removal.
    """
    raise NotImplementedError("Gaetano: implement A* search")
