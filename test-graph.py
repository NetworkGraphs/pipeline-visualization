import graph_utils as gutl
import utils as utl
from containers import run

graph = {
    "nodes": [
        {"id": "A", "label": "Node A"},
        {"id": "B", "label": "Node B"},
        {"id": "C", "label": "Node C"}
    ],
    "edges": [
        {"source": "A", "target": "B", "label": "A to B"},
        {"source": "B", "target": "C", "label": "B to C"}
    ]
}

dot = gutl.graph_to_dot(graph)

utl.save_text(dot,"cache/test/gen.dot")

run.graphviz("test/gen.dot")
