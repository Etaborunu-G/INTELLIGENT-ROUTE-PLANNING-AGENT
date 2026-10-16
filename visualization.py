"""Owner: Member 4. Graph drawing and route highlighting."""
from typing import TYPE_CHECKING
from models import Graph, SearchResult

if TYPE_CHECKING:
    from tkinter import Canvas


def draw_graph(canvas: "Canvas", graph: Graph,
               result: SearchResult | None = None) -> None:
    """TODO: scale positions, draw roads/nodes, clear and highlight result."""
    raise NotImplementedError("Member 4: implement graph visualization")
