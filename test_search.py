"""Basic A* and Greedy tests for the progress report."""

from astar import astar
from greedy import greedy


# Map 1: Only one route exists.
map1 = {
    "positions": {0: (0, 0), 1: (3, 0), 2: (6, 0)},
    "roads": {
        0: {1: 3.0},
        1: {0: 3.0, 2: 3.0},
        2: {1: 3.0},
    },
}

# Map 2: A* should find the cheaper route.
# Greedy should choose the direct road to the goal.
map2 = {
    "positions": {0: (0, 0), 1: (3, 0), 2: (6, 0)},
    "roads": {
        0: {1: 3.0, 2: 10.0},
        1: {0: 3.0, 2: 3.0},
        2: {0: 10.0, 1: 3.0},
    },
}

# Map 3: The goal is disconnected.
map3 = {
    "positions": {0: (0, 0), 1: (3, 0), 2: (6, 0)},
    "roads": {
        0: {1: 3.0},
        1: {0: 3.0},
        2: {},
    },
}

maps = [map1, map2, map3]

expected_astar = [
    ([0, 1, 2], 6.0, True),
    ([0, 1, 2], 6.0, True),
    ([], float("inf"), False),
]

expected_greedy = [
    ([0, 1, 2], 6.0, True),
    ([0, 2], 10.0, True),
    ([], float("inf"), False),
]

for i in range(3):
    print(f"\nMap {i + 1}")

    result = astar(maps[i], 0, 2)

    if "execution_time" in result and result["execution_time"] >= 0:
        print("Execution time: PASS")
        print("Seconds:", result["execution_time"])
    else:
        print("Execution time: FAIL — missing or negative")

    actual = (result["path"], result["cost"], result["success"])
    print("A*:", "PASS" if actual == expected_astar[i] else "FAIL")
    print("Expected:", expected_astar[i])
    print("Actual:  ", actual)

    result = greedy(maps[i], 0, 2)

    if "execution_time" in result and result["execution_time"] >= 0:
        print("Execution time: PASS")
        print("Seconds:", result["execution_time"])
    else:
        print("Execution time: FAIL — missing or negative")
        
    actual = (result["path"], result["cost"], result["success"])
    print("Greedy:", "PASS" if actual == expected_greedy[i] else "FAIL")
    print("Expected:", expected_greedy[i])
    print("Actual:  ", actual)