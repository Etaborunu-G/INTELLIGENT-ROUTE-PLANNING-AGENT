"""Member 3: run comparisons, save CSV measurements and make charts.
Everyone helps interpret the results.
"""
from map_generator import generate_map
from ucs import ucs
from greedy import greedy
from astar import astar


def run_experiments():
    # TODO: change one setting at a time and repeat across several seeds.
    # Generate each graph once; reuse it and its start/goal for all algorithms.
    # Compare UCS, Greedy, A*, and A* with use_heuristic=False.
    # Save settings, seed, start, goal, algorithm and result metrics to CSV.
    raise NotImplementedError("Member 3: implement the experiments")


if __name__ == "__main__":
    run_experiments()
