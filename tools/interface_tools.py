import networkx as nx
from tools.graph_tools import generate_matrix, draw_graph


def show_graph_algos(boolean_variable, ui):
    ui.algos_arbre.hide()
    ui.algos_graph.show()


def show_arbre_algos(boolean_variable, ui):
    ui.algos_graph.hide()
    ui.algos_arbre.show()


def generate_new_graph(boolean_variable, ui):
    nb_nodes = ui.nb_nodes.value()
    ui.matrix = generate_matrix(nb_nodes)
    graph = nx.from_numpy_matrix(ui.matrix)

    ui.InitFig.canvas.axes.clear()
    draw_graph(graph, axis=ui.InitFig.canvas.axes)
    ui.InitFig.canvas.draw()
