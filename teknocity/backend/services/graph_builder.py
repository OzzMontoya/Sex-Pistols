import networkx as nx


def build_graph(intersections, roads):
    graph = nx.DiGraph()

    for node in intersections:
        graph.add_node(node["id"], state=node.get("state", {}))

    for edge in roads:
        graph.add_edge(edge["from"], edge["to"], **edge.get("metadata", {}))

    return graph
