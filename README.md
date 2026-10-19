# Intelligent Route-Planning Agent

SOFE 3720U Group 2 school project. We will compare Uniform Cost Search,
Greedy Best-First Search and A* on randomly generated road networks.

## Getting started

Use Python 3.11 and run from this folder:

```bash
python main.py
```

This is a starter project. Running main.py currently prints a status message.
The maps, algorithms, interface and experiments are still TODO. Unfinished
functions raise NotImplementedError instead of returning made-up results.
Only Python's standard library is needed for now. We can use Tkinter for the
interface; it may need to be installed separately on Linux. Add a requirements.txt
later if we choose an external plotting library.

## Who does what

| File | Owner | Work |
| --- | --- | --- |
| main.py | Member 4 | Controls, map drawing and result display |
| map_generator.py | Member 2 | Generate and check the road network |
| ucs.py | Member 3 | Uniform Cost Search |
| greedy.py | Member 4 | Greedy Best-First Search |
| astar.py | Gaetano | A* and heuristic functions |
| experiments.py | Member 3 | Run comparisons, save CSV and make initial charts |
| README.md | Everyone | Setup, roles and shared rules |

Gaetano coordinates how the files connect. Each person tests, connects and fixes
their own code. Everyone helps analyse results and prepare the presentation.
Replace Member 2–4 with names when the group assigns them. Redistribute remaining
work if one role takes substantially longer. Keep the interface simple.

## How the files connect

main.py calls generate_map and then the chosen search function. It draws the
returned path and shows the metrics. experiments.py calls the same functions
without opening the interface. Greedy imports straight_line_distance from
astar.py so the two algorithms use the same estimate. astar.py does not import
main.py or greedy.py. No separate models or dispatcher are needed.

## The map dictionary

All files use this format. This is a small valid example:

```python
graph = {
    "positions": {0: (0, 0), 1: (3, 0), 2: (3, 4)},
    "roads": {
        0: {1: 3.0, 2: 7.0},
        1: {0: 3.0, 2: 4.0},
        2: {0: 7.0, 1: 4.0},
    },
}
```

A node is an intersection. Its position is its (x, y) coordinate. A road is an
edge and its value is the travel cost. Roads go both ways with the same cost.
Every node appears in both dictionaries, even if it has no roads. Coordinates
must be unique and finite; costs must be finite and positive. A road's cost is
its straight-line length multiplied by a factor of at least 1. This makes the
straight-line heuristic a valid lower bound. Crossing road lines only connect
if the graph explicitly includes an intersection there.

Use graph["positions"][node] for coordinates and graph["roads"][node].items()
for neighbours and costs. Do not change the graph while searching.

## Search inputs and results

```python
ucs(graph, start, goal)
greedy(graph, start, goal)
astar(graph, start, goal, use_heuristic=True)
```

Every algorithm returns the same dictionary:

```python
result = {
    "path": [0, 1, 2],
    "cost": 7.0,
    "nodes_expanded": 2,
    "execution_time": 0.001,
    "success": True,
}
```

This result is illustrative, not a measured run. Path means an ordered list of
nodes; cost means the sum of its road costs. If no route exists, return an empty
path, float("inf") for cost and success=False. If start equals goal, return
[start], zero cost, zero expansions and success=True. Invalid node IDs or
settings raise ValueError.

Count an expansion when a valid non-goal node's neighbours are examined. Do not
count stale queue entries or the goal; count another expansion if a node is
reopened. Measure search setup, search and reconstruction with time.perf_counter
in seconds, excluding map generation, drawing and writing results.

## Terms and simple coding rules

- Use snake_case names, four spaces and short comments explaining tricky parts.
- start and goal are node IDs; neighbour is a connected node.
- frontier is the priority queue; came_from stores each node's parent.
- g_score stores best costs from the start; heuristic estimates remaining cost.
- UCS uses cost so far, Greedy uses the estimate, and A* uses their sum.
- Use heapq for queues. Sort neighbours and use a counter for consistent ties.
- UCS/A* update costs and parents only for cheaper paths and skip stale records.
  Check for the goal after removing a valid queue entry, not on first discovery.
- Use random.Random(seed) to reproduce maps. Keep costs unrounded internally.
- Write the primary search logic ourselves. Supporting drawing/CSV libraries are OK.
- Keep printing, controls and drawing in main.py, outside the search functions.
- Use a branch for your task. Ask a teammate to review before merging and discuss
  shared format changes before changing other people's code.

## Testing and experiments

Start with hand-written maps where the answer is known. Check every returned
road and add up the cost. UCS and A* should return the optimal cost; equal-cost
paths may differ. Compare floats with math.isclose. Greedy only needs a valid
route. Check cycles, cheaper routes with more edges, disconnected goals,
isolated nodes, start=goal and invalid input. Each owner checks their own code;
Member 3 coordinates comparisons.

Vary graph size, road density, road-cost variation and start/goal distance. Use
several seeds, hold the graph and start/goal fixed across algorithms, and repeat
timings. Record seed, map settings, start, goal, algorithm, heuristic mode, cost,
nodes_expanded, execution_time and success in CSV. Keep results in results/.
Compare A* with and without its heuristic. Report failures separately from costs
of successful routes, and explain the trade-off between search effort and cost.

Progress presentation: week of October 19, 2026. Final presentation and separate
demonstration: week of November 30, 2026, according to the project handout.
