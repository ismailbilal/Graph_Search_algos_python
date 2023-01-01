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
    ui.algos_arbre.hide()
    ui.nb_nodes.setValue(12)
    ui.algorithm_name.setText('Bellman-Ford')
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(100)
    shadow.setColor(QColor("gray"))
    ui.header.setGraphicsEffect(shadow)
    ui.isTree = False

    # button handlers
    ui.graph_btn.clicked.connect(lambda bol: interface_tools.show_graph_algos(bol, ui))
    ui.arbre_btn.clicked.connect(lambda bol: interface_tools.show_arbre_algos(bol, ui))
    ui.generate_btn.clicked.connect(lambda bol: interface_tools.draw_new_tree(bol, ui) if ui.isTree else interface_tools.draw_new_graph(bol, ui))

    MainWindow.show()
    sys.exit(app.exec_())
