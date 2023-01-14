import networkx as nx
from random import choice, randint
from numpy import matrix


def generate_matrix(nb_nodes=10, min_value=1, max_value=18):
    random_graph = matrix(
        [[choice([0, 0, 0, 1]) * randint(min_value, max_value) for j in range(nb_nodes)] for i in range(nb_nodes)])
    for i in range(nb_nodes):
        random_graph[i, i] = 0
        for j in range(i):
            random_graph[i, j] = random_graph[j, i]
    return random_graph


def draw_network(graph, start_node=None, goal_node=None, path_edges=None, axis="off", with_edge_labels=True, pos=None):
    if path_edges is None:
        path_edges = []
    node_size = 200 + 2000 / graph.number_of_nodes() ** 1.5  # 200
    font_size = 7 + 16 / graph.number_of_nodes()  # 7
    edge_labels = nx.get_edge_attributes(graph, "weight")

    # position of all nodes
    if not pos:
        pos = nx.spring_layout(graph, seed=0)
    # draw all nodes
    nx.draw_networkx_nodes(graph, pos, node_color="tab:blue", node_size=node_size, ax=axis)
    # draw starting node with the color green
    if start_node is not None:
        nx.draw_networkx_nodes(graph, pos, nodelist=[start_node], node_color="tab:green", node_size=node_size, ax=axis)
    # draw goal_node with the color red
    if goal_node is not None:
        nx.draw_networkx_nodes(graph, pos, nodelist=[goal_node], node_color="tab:red", node_size=node_size, ax=axis)
    # draw all edges
    nx.draw_networkx_edges(graph, pos, width=1, ax=axis)
    if path_edges:
        nx.draw_networkx_edges(
            graph, pos, edgelist=path_edges, width=3, alpha=0.5, edge_color="red", style="solid", ax=axis
        )
    # draw edges attributes
    if with_edge_labels:
        nx.draw_networkx_edge_labels(graph, pos, edge_labels, font_size=font_size, ax=axis)
    nx.draw_networkx_labels(graph, pos, font_size=font_size, font_family="sans-serif", font_color="white", ax=axis)


def to_unit_matrix(np_matrix):
    new_matrix = np_matrix.copy()
    new_matrix[new_matrix > 0] = 1
    return new_matrix
