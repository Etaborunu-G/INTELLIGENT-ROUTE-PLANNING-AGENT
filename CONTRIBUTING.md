# Coding agreement

- Python 3.11, four spaces, snake_case functions/files, PascalCase classes.
- Import contracts from models.py. Discuss field/signature changes before editing callers.
- Graphs are undirected, coordinates unique and finite, and costs finite/positive.
  Each edge cost is at least Euclidean distance. No self-loops. Include isolated nodes.
- Search functions never mutate the graph, draw, prompt, or write files.
- Use heapq, sorted neighbours and a monotonic counter for deterministic queue ties.
- UCS/A*: improve best costs and parents; skip stale entries; test goal on valid pop.
- Count only non-goal nodes whose neighbours are examined. Exclude stale entries.
- Time initialization, search and reconstruction with time.perf_counter; use seconds.
- No solution: empty path, infinite cost, success=False. Start=goal: [start], zero cost
  and expansions. Invalid IDs/settings raise ValueError.
- Compare float costs with math.isclose. Equal-cost optimal paths may differ.
- Generate with random.Random(seed). Keep the exact graph and start/goal fixed
  across algorithms. Do not call library implementations of the core searches.
- Use feature branches, clear commits and one teammate review before merging.
  Each owner tests, integrates and fixes their component. Leadership coordinates work.
- Everyone explains their findings and understands all three algorithms.

## Review and verification

Run `python -m unittest discover -v` and `python -m compileall -q .`.
Current automated checks cover scaffold contracts only. Implement real algorithm
correctness tests before claiming the system works; never replace TODOs with fake results.
