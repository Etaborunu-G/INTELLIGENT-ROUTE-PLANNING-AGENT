"""Gaetano: A* and the shared straight-line heuristic."""
import math
import heapq
import itertools
import time


def straight_line_distance(graph, node, goal):
    """Return the straight-line distance from a node to the goal node."""
    x1, y1 = graph["positions"][node]
    x2, y2 = graph["positions"][goal]

    return math.hypot(x2 - x1, y2 - y1)


def astar(graph, start, goal, use_heuristic=True):
    """Find a minimum-cost route using A* search."""
    start_time = time.perf_counter()

    if start not in graph["roads"] or goal not in graph["roads"]:
        raise ValueError("Start and goal must exist in the graph.")

    frontier = []
    counter = itertools.count()
    came_from = {}
    g_score = {start: 0.0}
    nodes_expanded = 0

    if use_heuristic:
        h_value = straight_line_distance(graph, start, goal)
    else:
        h_value = 0.0

    priority = g_score[start] + h_value

    heapq.heappush(
        frontier,
        (priority, next(counter), start, g_score[start])
    )

    while frontier:
        priority, _, node, cost_so_far = heapq.heappop(frontier)

        if cost_so_far > g_score[node]:
            continue

        if node == goal:
            path = [goal]

            while path[-1] != start:
                parent = came_from[path[-1]]
                path.append(parent)

            path.reverse()

            return {
                "path": path,
                "cost": cost_so_far,
                "nodes_expanded": nodes_expanded,
                "execution_time": time.perf_counter() - start_time,
                "success": True,
            }

        nodes_expanded += 1

        for neighbour, edge_cost in sorted(graph["roads"][node].items()):
            new_cost = cost_so_far + edge_cost

            if new_cost < g_score.get(neighbour, float("inf")):
                g_score[neighbour] = new_cost
                came_from[neighbour] = node

                if use_heuristic:
                    h_value = straight_line_distance(graph, neighbour, goal)
                else:
                    h_value = 0.0

                priority = new_cost + h_value

                heapq.heappush(
                    frontier,
                    (priority, next(counter), neighbour, new_cost)
                )

    return {
        "path": [],
        "cost": float("inf"),
        "nodes_expanded": nodes_expanded,
        "execution_time": time.perf_counter() - start_time,
        "success": False,
    }