"""Inshal Chauhdry: Greedy Best-First Search."""
import heapq
import time
from astar import straight_line_distance


def greedy(graph, start, goal):
    """Return the result dictionary described in README.md.

    Prioritizes straight_line_distance(graph, node, goal).
    Tracks visited nodes to avoid cycles. Reconstructs and costs the path.
    Greedy is allowed to return a valid path that is not the cheapest.
    """
    # Priority queue stores tuples of (heuristic_value, current_node)
    start_time = time.perf_counter() # Record the start time

    if start not in graph["roads"] or goal not in graph["roads"]:
        raise ValueError("Start and goal must exist in the graph.") #if start node or goal does not exist, error
    
    pq = []
    start_h = straight_line_distance(graph, start, goal)
    heapq.heappush(pq, (start_h, start))

    visited = set()
    parent = {start: None}
    g_cost = {start: 0}  # Tracks cumulative path cost
    nodes_expanded = 0

    while pq:
        _, current = heapq.heappop(pq)

        if current == goal:
            # Reconstruct the path from goal to start
            path = []
            curr = goal
            while curr is not None:
                path.append(curr)
                curr = parent[curr]
            path.reverse()

            return {
                "success": True,
                "path": path,
                "cost": g_cost[goal],
                "nodes_expanded": nodes_expanded,
                "execution_time": time.perf_counter() - start_time,
            }

        if current in visited:
            continue

        visited.add(current)
        nodes_expanded += 1

        # Explore neighboring intersections
        for neighbor, weight in sorted(graph["roads"][current].items()):
            if neighbor not in visited:
                if neighbor not in parent or g_cost[current] + weight < g_cost.get(neighbor, float('inf')):
                    parent[neighbor] = current
                    g_cost[neighbor] = g_cost[current] + weight
                    h_val = straight_line_distance(graph, neighbor, goal)
                    heapq.heappush(pq, (h_val, neighbor))

    return {
        "success": False,
        "path": [],
        "cost": float('inf'),
        "nodes_expanded": nodes_expanded,
        "execution_time": time.perf_counter() - start_time,
    }
