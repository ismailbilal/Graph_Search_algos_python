import networkx as nx
from tools.graph_tools import generate_matrix, draw_network
from tools.tree_tools import generate_tree, hierarchy_pos
from algorithms.algorithms import algorithms


# selected_algo_btn_style = "border: none; font-weight: bold; background-color: #fff"


def show_graph_algos(boolean_variable, ui):
    if ui.isTree:
        ui.algos_arbre.hide()
        ui.algos_graph.show()
        clear_figures(ui)
        ui.nb_nodes.setValue(10)
        select_algo(False, ui, ui.bellmanford)
        ui.isTree = False


def show_arbre_algos(boolean_variable, ui):
    if not ui.isTree:
        ui.algos_graph.hide()
        ui.algos_arbre.show()
        clear_figures(ui)
        ui.nb_nodes.setValue(16)
        select_algo(False, ui, ui.prefixe)
        ui.isTree = True
        ui.start_node.setValue(0)


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
    ui.graph = graph

    ui.InitFig.canvas.axes.clear()
    ui.ResultFig.canvas.axes.clear()
    set_figures_style(ui)

    draw_network(graph, axis=ui.InitFig.canvas.axes)
    ui.InitFig.canvas.draw()

    draw_network(graph, axis=ui.ResultFig.canvas.axes)
    ui.ResultFig.canvas.draw()


def draw_new_tree(boolean_variable, ui):
    tree = generate_tree(ui.nb_nodes.value())
    ui.tree = tree
    pos = hierarchy_pos(tree, 0)
    ui.InitFig.canvas.axes.clear()
    ui.ResultFig.canvas.axes.clear()
    set_figures_style(ui)
    draw_network(tree, pos=pos, axis=ui.InitFig.canvas.axes)
    ui.InitFig.canvas.draw()
    draw_network(tree, pos=pos, axis=ui.ResultFig.canvas.axes)
    ui.ResultFig.canvas.draw()


def reset_algo_btns_style(ui):
    style = """
        QPushButton {
            border-right: 4px solid rgb(24, 112, 255);
            background-color: rgba(0,0,0,0%);
        }
        QPushButton:hover {
            background-color: #fff;
    """
    ui.infixe.setStyleSheet(style)
    ui.largeur.setStyleSheet(style)
    ui.postfixe.setStyleSheet(style)
    ui.prefixe.setStyleSheet(style)
    ui.profondeur.setStyleSheet(style)
    ui.astar.setStyleSheet(style)
    ui.bellmanford.setStyleSheet(style)
    ui.belmanfordmoore.setStyleSheet(style)
    ui.bfs.setStyleSheet(style)
    ui.dfs.setStyleSheet(style)
    ui.floydwarchal.setStyleSheet(style)
    ui.fordfulkerson.setStyleSheet(style)
    ui.kraskal.setStyleSheet(style)


def select_algo(boolean_variable, ui, algo_btn):
    ui.algorithm_name.setText(algo_btn.text())
    ui.algorithm_name.setStyleSheet("font-size:24px; color:rgb(18, 104, 255)")
    ui.algorithm_name.setEnabled(False)
    reset_algo_btns_style(ui)
    algo_btn.setStyleSheet('QPushButton#' + algo_btn.objectName() + """ {
            background-color: #fff;
            border: 3px solid rgba(0, 0, 0, 0);
            color: #000;
            font-weight: bold;
    }""")
    ui.current_algorithm = algo_btn.objectName()


def show_result(boolean_variable, ui):
    algo = ui.current_algorithm
    ui.ResultFig.canvas.axes.clear()
    set_figures_style(ui)
    if ui.isTree:
        tree_as_dict = nx.to_dict_of_lists(ui.tree)
        path = algorithms[algo]["algo_func"](tree_as_dict, ui.start_node.value())
        edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        DG = nx.DiGraph()
        DG.add_edges_from(edges)
        draw_network(DG, axis=ui.ResultFig.canvas.axes, path_edges=edges)
    else:
        if algo in ('kraskal'):
            tree = algorithms[algo]["algo_func"](ui.matrix.tolist())
            posTree = hierarchy_pos(tree, 0)
            draw_network(tree, pos=posTree, axis=ui.ResultFig.canvas.axes)
        else:
            path = algorithms[algo]["algo_func"](ui.matrix, ui.start_node.value(), ui.but_node.value())
            path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
            draw_network(ui.graph, axis=ui.ResultFig.canvas.axes, path_edges=path_edges,
                         start_node=ui.start_node.value(),
                         goal_node=ui.but_node.value())
    ui.ResultFig.canvas.draw()


def change_default_start_end(boolean_variable, ui):
    ui.start_node.setValue(0)
    ui.but_node.setValue(ui.nb_nodes.value() - 1)
