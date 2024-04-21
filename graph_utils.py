
def int_to_alphabet(n):
    """
    Converts an integer to a string where numbers are mapped as follows:
    1 -> A, 2 -> B, ..., 26 -> Z, 27 -> AA, 28 -> AB, and so on.
    """
    result = []
    while n > 0:
        n -= 1  # Decrement n by 1 to make the modulus operation zero-indexed
        remainder = n % 26
        result.append(chr(remainder + 65))  # 65 is the ASCII value for 'A'
        n = n // 26  # Move to the next 'digit'
    
    return ''.join(reversed(result))

def graph_to_dot(graph):
    dot_string = "digraph G {\n"
    nodes_map = {}
    for index,node in enumerate(graph["nodes"],1):
        nodes_map[node["label"]] = int_to_alphabet(index)
    for node in graph["nodes"]:
        label = node["label"]
        node_class = node["class"]
        node_shape = shapes_map[node_class]
        dot_string += f'    {nodes_map[label]} [label="{label}", class="{node_class}", shape="{node_shape}"];\n'
    for edge in graph["edges"]:
        source = nodes_map[edge["source"]]
        target = nodes_map[edge["target"]]
        dot_string += f'    {source} -> {target};\n'
    dot_string += "}"
    return dot_string

def add_edge(source,target):
    global graph
    if(source not in graph["nodes"]):
        graph["nodes"].append(source)
    if(target not in graph["nodes"]):
        graph["nodes"].append(target)
    graph["edges"].append({
        "source":source["label"],
        "target":target["label"]
    })
    return

def get_dot_graph(graph):
    dot_string = graph_to_dot(graph)
    return dot_string

def get_graph():
    global graph
    return graph

graph = {
    "nodes":[],
    "edges":[]
}

shapes_map = {
    "job":"box",
    "artifact":"ellipse"
}
