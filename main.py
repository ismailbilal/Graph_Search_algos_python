from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import *
import sys
from interface.window_interface import Ui_MainWindow
from tools import interface_tools

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # initialize interface variables
    ui.textEdit.setEnabled(False)
    ui.algorithm_name.setEnabled(False)
    ui.isTree = True
    interface_tools.show_graph_algos(False, ui)
    ui.start_node.setValue(0)
    ui.but_node.setValue(ui.nb_nodes.value() - 1)

    # set default start node and end node
    ui.nb_nodes.valueChanged.connect(lambda bol: interface_tools.change_default_start_end(bol, ui))

    # button handlers
    ui.graph_btn.clicked.connect(lambda bol: interface_tools.show_graph_algos(bol, ui))
    ui.arbre_btn.clicked.connect(lambda bol: interface_tools.show_arbre_algos(bol, ui))
    ui.generate_btn.clicked.connect(
        lambda bol: interface_tools.draw_new_tree(bol, ui) if ui.isTree else interface_tools.draw_new_graph(bol, ui))
    ui.infixe.clicked.connect(lambda bol: interface_tools.select_algo(bol, ui, ui.infixe))
    ui.largeur.clicked.connect(lambda bol: interface_tools.select_algo(bol, ui, ui.largeur))
    ui.postfixe.clicked.connect(lambda bol: interface_tools.select_algo(bol, ui, ui.postfixe))
    ui.prefixe.clicked.connect(lambda bol: interface_tools.select_algo(bol, ui, ui.prefixe))
    ui.profondeur.clicked.connect(lambda bol: interface_tools.select_algo(bol, ui, ui.profondeur))
    ui.astar.clicked.connect(lambda bol: interface_tools.select_algo(bol, ui, ui.astar))
    ui.bellmanford.clicked.connect(lambda bol: interface_tools.select_algo(bol, ui, ui.bellmanford))
    ui.belmanfordmoore.clicked.connect(lambda bol: interface_tools.select_algo(bol, ui, ui.belmanfordmoore))
    ui.bfs.clicked.connect(lambda bol: interface_tools.select_algo(bol, ui, ui.bfs))
    ui.dfs.clicked.connect(lambda bol: interface_tools.select_algo(bol, ui, ui.dfs))
    ui.floydwarchal.clicked.connect(lambda bol: interface_tools.select_algo(bol, ui, ui.floydwarchal))
    ui.fordfulkerson.clicked.connect(lambda bol: interface_tools.select_algo(bol, ui, ui.fordfulkerson))
    ui.kraskal.clicked.connect(lambda bol: interface_tools.select_algo(bol, ui, ui.kraskal))
    ui.dijkstra.clicked.connect(lambda bol: interface_tools.select_algo(bol, ui, ui.dijkstra))

    ui.apply_btn.clicked.connect(lambda bol: interface_tools.show_result(bol, ui))

    MainWindow.show()
    sys.exit(app.exec_())
