import networkx as nx
from tools.graph_tools import generate_matrix, draw_graph
from tools.tree_tools import generate_tree, hierarchy_pos


# selected_algo_btn_style = "border: none; font-weight: bold; background-color: #fff"


def show_graph_algos(boolean_variable, ui):
    if ui.isTree:
        ui.algos_arbre.hide()
        ui.algos_graph.show()
        clear_figures(ui)
        ui.isTree = False


def show_arbre_algos(boolean_variable, ui):
    if not ui.isTree:
        ui.algos_graph.hide()
        ui.algos_arbre.show()
        clear_figures(ui)
        ui.isTree = True


def set_figures_style(ui):
    ui.InitFig.canvas.axes.set_title("Initial Network")
    ui.ResultFig.canvas.axes.set_title("Result")
    ui.InitFig.canvas.axes.axis("off")
    ui.ResultFig.canvas.axes.axis("off")


def clear_figures(ui):
    ui.InitFig.canvas.axes.clear()
    ui.ResultFig.canvas.axes.clear()
    set_figures_style(ui)
    ui.ResultFig.canvas.draw()
    ui.InitFig.canvas.draw()


def draw_new_graph(boolean_variable, ui):
    nb_nodes = ui.nb_nodes.value()
    ui.matrix = generate_matrix(nb_nodes)
    graph = nx.from_numpy_matrix(ui.matrix)

    ui.InitFig.canvas.axes.clear()
    ui.ResultFig.canvas.axes.clear()
    set_figures_style(ui)

    draw_graph(graph, axis=ui.InitFig.canvas.axes)
    ui.InitFig.canvas.draw()

    draw_graph(graph, axis=ui.ResultFig.canvas.axes)
    ui.ResultFig.canvas.draw()


def draw_new_tree(boolean_variable, ui):
    tree = generate_tree(ui.nb_nodes.value())
    pos = hierarchy_pos(tree, 0)
    ui.InitFig.canvas.axes.clear()
    ui.ResultFig.canvas.axes.clear()
    set_figures_style(ui)
    nx.draw(tree, pos=pos, with_labels=True, ax=ui.InitFig.canvas.axes)
    ui.InitFig.canvas.draw()
    nx.draw(tree, pos=pos, with_labels=True, ax=ui.ResultFig.canvas.axes)
    ui.ResultFig.canvas.draw()

# def select_algo(boolean_variable, ui, algo_btn):
#     algo_btn.setStyleSheet(selected_algo_btn_style)
