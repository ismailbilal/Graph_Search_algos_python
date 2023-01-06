import networkx as nx


def heuristic(graph, goal, ceof=1):
    return [(len(nx.astar_path(graph, source=node, target=goal)) - 1) * ceof for node in graph.nodes()]
