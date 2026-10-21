"""Member 3: Uniform Cost Search."""
import heapq
import itertools
import time

def ucs(graph, start, goal):
    """Find a minimum-cost route using Uniform Cost Search."""
    start_time = time.perf_counter()

    if start not in graph["roads"] or goal not in graph["roads"]:
        raise ValueError("Start and goal must exist in the graph.")

    frontier = []
    counter = itertools.count()
    came_from = {}
    g_score = {start: 0.0}
    nodes_expanded = 0

    heapq.heappush(frontier, (0.0, next(counter), start))

    while frontier:
        cost_so_far, _, node = heapq.heappop(frontier)

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

                heapq.heappush(
                    frontier,
                    (new_cost, next(counter), neighbour)
                )

    return {
        "path": [],
        "cost": float("inf"),
        "nodes_expanded": nodes_expanded,
        "execution_time": time.perf_counter() - start_time,
        "success": False,
    }