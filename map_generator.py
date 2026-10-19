"""Member 2: create the road network."""


def generate_map(num_nodes=50, edge_probability=0.1, seed=42,
                 min_multiplier=1.0, max_multiplier=3.0):
    """Return {"positions": {node: (x, y)}, "roads": {node: {neighbour: cost}}}.

    TODO: use random.Random(seed), unique coordinates and two-way roads.
    Every cost must be positive and at least the straight-line road length.
    Include isolated nodes. Reject invalid settings with ValueError.
    """
    raise NotImplementedError("Member 2: implement map generation")
