"""Inshal Chauhdry: Greedy Best-First Search."""
import heapq
from astar import straight_line_distance


def greedy(graph, start, goal):
    """Return the result dictionary described in README.md.

    Prioritizes straight_line_distance(graph, node, goal).
    Tracks visited nodes to avoid cycles. Reconstructs and costs the path.
    Greedy is allowed to return a valid path that is not the cheapest.
    """
    # Priority queue stores tuples of (heuristic_value, current_node)
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
                "nodes_expanded": nodes_expanded
            }

        if current in visited:
            continue

        visited.add(current)
        nodes_expanded += 1

        # Explore neighboring intersections
        for neighbor, weight in graph.get(current, {}).items():
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
        "nodes_expanded": nodes_expanded
    }
