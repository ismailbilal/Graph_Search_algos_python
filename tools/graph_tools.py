import networkx as nx
from random import choice, randint
from numpy import matrix


def generate_matrix(nb_nodes=10):
    min_value = 1
    max_value = 18
    random_graph = matrix(
        [[choice([0, 0, 0, 1]) * randint(min_value, max_value) for j in range(nb_nodes)] for i in range(nb_nodes)])
    for i in range(nb_nodes):
        random_graph[i, i] = 0
    return random_graph


def draw_graph(G, start_node=None, goal_node=None, figure_nb=1, path_edges=[], axis="off"):
    node_size = 200
    font_size = 7
    edge_labels = nx.get_edge_attributes(G, "weight")

    # position of all nodes
    pos = nx.spring_layout(G, seed=0)
    # draw all nodes
    nx.draw_networkx_nodes(G, pos, node_color="tab:blue", node_size=node_size, ax=axis)
    # draw starting node with the color green
    if start_node:
        nx.draw_networkx_nodes(G, pos, nodelist=[start_node], node_color="tab:green", node_size=node_size, ax=axis)
    # draw goal_node with the color red
    if goal_node:
        nx.draw_networkx_nodes(G, pos, nodelist=[goal_node], node_color="tab:red", node_size=node_size, ax=axis)
    # draw all edges
    nx.draw_networkx_edges(G, pos, width=1, ax=axis)
    if path_edges:
        nx.draw_networkx_edges(
            G, pos, edgelist=path_edges, width=3, alpha=0.5, edge_color="red", style="solid", ax=axis
        )
    # draw edges attributes
    nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=font_size, ax=axis)
    nx.draw_networkx_labels(G, pos, font_size=font_size, font_family="sans-serif", font_color="white", ax=axis)
