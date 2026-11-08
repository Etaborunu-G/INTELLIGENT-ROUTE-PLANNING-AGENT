"""Member 2: create the road network."""
import random
import math

def generate_map(num_nodes=50, edge_probability=0.1, seed=42,
                 min_multiplier=1.0, max_multiplier=3.0):
    
    """Generate a random road network with nodes, coordinates, and two-way roads.

    Returns a dictionary containing node positions and road connections.
    Road costs are based on straight-line distance and a random multiplier.
    """
    
    #Validate number of nodes
    if type(num_nodes) is not int or num_nodes < 1:
        raise ValueError("num_nodes must be a positive integer.")

    if type(edge_probability) not in (int, float) or not math.isfinite(edge_probability) or not 0 <= edge_probability <= 1:
        raise ValueError("edge_probability must be between 0 and 1.")

    if type(seed) is not int:
        raise ValueError("seed must be an integer.")

    #Validate cost multipliers
    if type(min_multiplier) not in (int, float) or not math.isfinite(min_multiplier) or min_multiplier < 1:
        raise ValueError("min_multiplier must be at least 1.")

    if type(max_multiplier) not in (int, float) or not math.isfinite(max_multiplier) or max_multiplier < min_multiplier:
        raise ValueError("max_multiplier must be greater than or equal to min_multiplier.")

    #Creates a random number generator
    rng = random.Random(seed)

    #Stores each node and its coordinates
    positions = {}
    used_coordinates = set()

    #Generate random positions for each node
    while len(positions) < num_nodes:
        x = rng.uniform(0, 100)
        y = rng.uniform(0, 100)

        coordinate = (x, y)

        if coordinate not in used_coordinates:
            node_id = len(positions)
            positions[node_id] = coordinate
            used_coordinates.add(coordinate)

    #Create an empty road dictionary for every node
    roads = {node: {} for node in positions}

    #Randomly connect pairs of nodes
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if rng.random() < edge_probability:
                #Gets the coordinates of both nodes
                x1, y1 = positions[i]
                x2, y2 = positions[j]

                #Calculates straight-line distance
                distance = math.hypot(x2 - x1, y2 - y1)

                #Generates a random road cost multiplier
                multiplier = rng.uniform(min_multiplier, max_multiplier)

                cost = distance * multiplier

                #Adds the road in both directions
                roads[i][j] = cost
                roads[j][i] = cost    

    return {
        "positions": positions,
        "roads": roads
    }

if __name__ == "__main__":
    graph = generate_map(num_nodes=5, edge_probability=0.5)

    print("Positions:")
    for node, (x, y) in graph["positions"].items():
        print(f"Node {node}: ({x:.2f}, {y:.2f})")

    print("\nRoads:")
    for node, neighbours in graph["roads"].items():
        formatted = {n: round(cost, 2) for n, cost in neighbours.items()}
        print(f"Node {node}: {formatted}")             
