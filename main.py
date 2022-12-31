from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sys
from interface.window_interface import Ui_MainWindow
from tools import interface_tools
from tools.interface_tools import generate_new_graph

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    # initialize interface variables
    ui.algos_arbre.hide()
    ui.nb_nodes.setValue(8)

    # button handlers
    ui.graph_btn.clicked.connect(lambda bol: interface_tools.show_graph_algos(bol, ui))
    ui.arbre_btn.clicked.connect(lambda bol: interface_tools.show_arbre_algos(bol, ui))
    ui.generate_btn.clicked.connect(lambda bol: generate_new_graph(bol, ui))

    MainWindow.show()
    sys.exit(app.exec_())
