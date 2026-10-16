"""Shared known-answer graph. Owner: Member 3."""
from models import Graph


def example_graph() -> Graph:
    """Optimal cost 0 to 2 is 7, with two equal-cost alternatives."""
    return Graph(
        positions={0: (0.0, 0.0), 1: (3.0, 0.0), 2: (3.0, 4.0)},
        adjacency={0: {1: 3.0, 2: 7.0}, 1: {0: 3.0, 2: 4.0},
                   2: {0: 7.0, 1: 4.0}},
    )
