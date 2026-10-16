"""Owner: Member 3. Controlled batch execution and CSV export."""
from pathlib import Path

CSV_FIELDS = (
    "instance_id", "seed", "num_nodes", "edge_probability", "coordinate_limit",
    "min_cost_multiplier", "max_cost_multiplier", "start", "goal", "algorithm",
    "heuristic", "repeat", "success", "cost", "nodes_expanded", "execution_time",
)


def run_experiments(config_path: Path, output_path: Path) -> None:
    """TODO: load JSON, build each instance once, run all algorithms, save CSV.

    Warm up before timed repeats. Exclude generation/drawing from search time.
    Record unreachable instances normally and input errors separately.
    """
    raise NotImplementedError("Member 3: implement experiment runner")
