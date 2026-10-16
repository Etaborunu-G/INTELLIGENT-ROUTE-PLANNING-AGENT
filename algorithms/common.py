"""Owner: Member 3. Helpers shared by all algorithms."""
from models import NodeId


def reconstruct_path(came_from: dict[NodeId, NodeId],
                     start: NodeId, goal: NodeId) -> list[NodeId]:
    """TODO: return ordered start-to-goal nodes using predecessor records."""
    raise NotImplementedError("Member 3: implement path reconstruction")
