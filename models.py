"""Shared contracts. Owner: Member 2; changes require team review."""
from dataclasses import dataclass
from typing import Callable

NodeId = int
Position = tuple[float, float]


@dataclass
class Graph:
    positions: dict[NodeId, Position]
    adjacency: dict[NodeId, dict[NodeId, float]]


@dataclass(frozen=True)
class MapConfig:
    num_nodes: int = 50
    edge_probability: float = 0.10
    coordinate_limit: float = 100.0
    min_cost_multiplier: float = 1.0
    max_cost_multiplier: float = 3.0
    seed: int = 42


@dataclass
class SearchResult:
    path: list[NodeId]
    cost: float
    nodes_expanded: int
    execution_time: float
    success: bool


Heuristic = Callable[[Graph, NodeId, NodeId], float]
