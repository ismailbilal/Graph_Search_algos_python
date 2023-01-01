import networkx as nx
from tools.graph_tools import generate_matrix, draw_graph
from tools.tree_tools import generate_tree, hierarchy_pos


# selected_algo_btn_style = "border: none; font-weight: bold; background-color: #fff"


def show_graph_algos(boolean_variable, ui):
    if ui.isTree:
        ui.algos_arbre.hide()
        ui.algos_graph.show()
        ui.InitFig.canvas.axes.clear()
        ui.InitFig.canvas.draw()
        ui.ResultFig.canvas.axes.clear()
        ui.ResultFig.canvas.draw()
        ui.isTree = False


def show_arbre_algos(boolean_variable, ui):
    if not ui.isTree:
        ui.algos_graph.hide()
        ui.algos_arbre.show()
        ui.InitFig.canvas.axes.clear()
        ui.InitFig.canvas.draw()
        ui.ResultFig.canvas.axes.clear()
        ui.ResultFig.canvas.draw()
        ui.isTree = True


def draw_new_graph(boolean_variable, ui):
    nb_nodes = ui.nb_nodes.value()
    ui.matrix = generate_matrix(nb_nodes)
    graph = nx.from_numpy_matrix(ui.matrix)

    ui.InitFig.canvas.axes.clear()
    draw_graph(graph, axis=ui.InitFig.canvas.axes)
    ui.InitFig.canvas.draw()

    ui.ResultFig.canvas.axes.clear()
    draw_graph(graph, axis=ui.ResultFig.canvas.axes)
    ui.ResultFig.canvas.draw()


def draw_new_tree(boolean_variable, ui):
    tree = generate_tree(ui.nb_nodes.value())
    pos = hierarchy_pos(tree, 0)
    ui.InitFig.canvas.axes.clear()
    ui.ResultFig.canvas.axes.clear()
    nx.draw(tree, pos=pos, with_labels=True, ax=ui.InitFig.canvas.axes)
    ui.InitFig.canvas.draw()
    nx.draw(tree, pos=pos, with_labels=True, ax=ui.ResultFig.canvas.axes)
    ui.ResultFig.canvas.draw()

# def select_algo(boolean_variable, ui, algo_btn):
#     algo_btn.setStyleSheet(selected_algo_btn_style)
