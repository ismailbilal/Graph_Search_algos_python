# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1422, 772)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.main = QtWidgets.QFrame(self.centralwidget)
        self.main.setMinimumSize(QtCore.QSize(1200, 700))
        self.main.setToolTipDuration(-1)
        self.main.setStyleSheet("border: 0px solid rgb(255, 255, 255);\n"
"background-color: rgb(73, 67, 138);\n"
"color: rgb(255, 255, 255)")
        self.main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main.setObjectName("main")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.main)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.header = QtWidgets.QFrame(self.main)
        self.header.setMinimumSize(QtCore.QSize(0, 70))
        self.header.setMaximumSize(QtCore.QSize(16777215, 60))
        self.header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")
        self.verticalLayout_5.addWidget(self.header)
        self.mainbody = QtWidgets.QFrame(self.main)
        self.mainbody.setStyleSheet("background-color: rgb(116, 112, 178)")
        self.mainbody.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainbody.setFrameShadow(QtWidgets.QFrame.Raised)
        self.mainbody.setObjectName("mainbody")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.mainbody)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.algos = QtWidgets.QFrame(self.mainbody)
        self.algos.setMaximumSize(QtCore.QSize(150, 16777215))
        self.algos.setStyleSheet("background-color: rgb(95, 94, 163)")
        self.algos.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.algos.setFrameShadow(QtWidgets.QFrame.Raised)
        self.algos.setObjectName("algos")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.algos)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.algos_graph = QtWidgets.QFrame(self.algos)
        self.algos_graph.setStyleSheet("")
        self.algos_graph.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.algos_graph.setFrameShadow(QtWidgets.QFrame.Raised)
        self.algos_graph.setObjectName("algos_graph")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.algos_graph)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.bellmanford = QtWidgets.QPushButton(self.algos_graph)
        self.bellmanford.setMinimumSize(QtCore.QSize(0, 30))
        self.bellmanford.setObjectName("bellmanford")
        self.verticalLayout_2.addWidget(self.bellmanford)
        self.floydwarchal = QtWidgets.QPushButton(self.algos_graph)
        self.floydwarchal.setMinimumSize(QtCore.QSize(0, 30))
        self.floydwarchal.setObjectName("floydwarchal")
        self.verticalLayout_2.addWidget(self.floydwarchal)
        self.belmanfordmoore = QtWidgets.QPushButton(self.algos_graph)
        self.belmanfordmoore.setMinimumSize(QtCore.QSize(0, 30))
        self.belmanfordmoore.setObjectName("belmanfordmoore")
        self.verticalLayout_2.addWidget(self.belmanfordmoore)
        self.fordfulkerson = QtWidgets.QPushButton(self.algos_graph)
        self.fordfulkerson.setMinimumSize(QtCore.QSize(0, 30))
        self.fordfulkerson.setObjectName("fordfulkerson")
        self.verticalLayout_2.addWidget(self.fordfulkerson)
        self.kraskal = QtWidgets.QPushButton(self.algos_graph)
        self.kraskal.setMinimumSize(QtCore.QSize(0, 30))
        self.kraskal.setObjectName("kraskal")
        self.verticalLayout_2.addWidget(self.kraskal)
        self.astar = QtWidgets.QPushButton(self.algos_graph)
        self.astar.setMinimumSize(QtCore.QSize(0, 30))
        self.astar.setObjectName("astar")
        self.verticalLayout_2.addWidget(self.astar)
        self.bfs = QtWidgets.QPushButton(self.algos_graph)
        self.bfs.setMinimumSize(QtCore.QSize(0, 30))
        self.bfs.setObjectName("bfs")
        self.verticalLayout_2.addWidget(self.bfs)
        self.dfs = QtWidgets.QPushButton(self.algos_graph)
        self.dfs.setMinimumSize(QtCore.QSize(0, 30))
        self.dfs.setObjectName("dfs")
        self.verticalLayout_2.addWidget(self.dfs)
        self.verticalLayout_6.addWidget(self.algos_graph)
        self.algos_arbre = QtWidgets.QFrame(self.algos)
        self.algos_arbre.setStyleSheet("")
        self.algos_arbre.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.algos_arbre.setFrameShadow(QtWidgets.QFrame.Raised)
        self.algos_arbre.setObjectName("algos_arbre")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.algos_arbre)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.prefixe = QtWidgets.QPushButton(self.algos_arbre)
        self.prefixe.setMinimumSize(QtCore.QSize(0, 30))
        self.prefixe.setObjectName("prefixe")
        self.verticalLayout_3.addWidget(self.prefixe)
        self.infixe = QtWidgets.QPushButton(self.algos_arbre)
        self.infixe.setMinimumSize(QtCore.QSize(0, 30))
        self.infixe.setObjectName("infixe")
        self.verticalLayout_3.addWidget(self.infixe)
        self.postfixe = QtWidgets.QPushButton(self.algos_arbre)
        self.postfixe.setMinimumSize(QtCore.QSize(0, 30))
        self.postfixe.setObjectName("postfixe")
        self.verticalLayout_3.addWidget(self.postfixe)
        self.largeur = QtWidgets.QPushButton(self.algos_arbre)
        self.largeur.setMinimumSize(QtCore.QSize(0, 30))
        self.largeur.setObjectName("largeur")
        self.verticalLayout_3.addWidget(self.largeur)
        self.profondeur = QtWidgets.QPushButton(self.algos_arbre)
        self.profondeur.setMinimumSize(QtCore.QSize(0, 30))
        self.profondeur.setObjectName("profondeur")
        self.verticalLayout_3.addWidget(self.profondeur)
        self.verticalLayout_6.addWidget(self.algos_arbre)
        self.horizontalLayout.addWidget(self.algos)
        self.show = QtWidgets.QFrame(self.mainbody)
        self.show.setStyleSheet("")
        self.show.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.show.setFrameShadow(QtWidgets.QFrame.Raised)
        self.show.setObjectName("show")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.show)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.generate = QtWidgets.QFrame(self.show)
        self.generate.setMinimumSize(QtCore.QSize(0, 80))
        self.generate.setMaximumSize(QtCore.QSize(16777215, 80))
        self.generate.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.generate.setFrameShadow(QtWidgets.QFrame.Raised)
        self.generate.setObjectName("generate")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.generate)
        self.horizontalLayout_4.setSpacing(300)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.type = QtWidgets.QFrame(self.generate)
        self.type.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.type.setFrameShadow(QtWidgets.QFrame.Raised)
        self.type.setObjectName("type")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.type)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame = QtWidgets.QFrame(self.type)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.nbnode_label = QtWidgets.QLabel(self.frame)
        self.nbnode_label.setToolTip("")
        self.nbnode_label.setObjectName("nbnode_label")
        self.horizontalLayout_6.addWidget(self.nbnode_label, 0, QtCore.Qt.AlignLeft)
        self.nb_nodes = QtWidgets.QSpinBox(self.frame)
        self.nb_nodes.setObjectName("nb_nodes")
        self.horizontalLayout_6.addWidget(self.nb_nodes, 0, QtCore.Qt.AlignLeft)
        self.generate_btn = QtWidgets.QPushButton(self.frame)
        self.generate_btn.setObjectName("generate_btn")
        self.horizontalLayout_6.addWidget(self.generate_btn)
        self.horizontalLayout_3.addWidget(self.frame)
        self.horizontalLayout_4.addWidget(self.type)
        self.frame_2 = QtWidgets.QFrame(self.generate)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.arbre = QtWidgets.QPushButton(self.frame_2)
        self.arbre.setMinimumSize(QtCore.QSize(0, 0))
        self.arbre.setStyleSheet("")
        self.arbre.setAutoDefault(False)
        self.arbre.setObjectName("arbre")
        self.horizontalLayout_5.addWidget(self.arbre)
        self.graph = QtWidgets.QPushButton(self.frame_2)
        self.graph.setStyleSheet("")
        self.graph.setObjectName("graph")
        self.horizontalLayout_5.addWidget(self.graph)
        self.horizontalLayout_4.addWidget(self.frame_2)
        self.verticalLayout_4.addWidget(self.generate)
        self.drawing = QtWidgets.QFrame(self.show)
        self.drawing.setStyleSheet("background-color: rgb(160, 156, 204);")
        self.drawing.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.drawing.setFrameShadow(QtWidgets.QFrame.Raised)
        self.drawing.setObjectName("drawing")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.drawing)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.InitFig = InitFig(self.drawing)
        self.InitFig.setMaximumSize(QtCore.QSize(550, 400))
        self.InitFig.setObjectName("InitFig")
        self.horizontalLayout_2.addWidget(self.InitFig)
        self.result_widget = QtWidgets.QWidget(self.drawing)
        self.result_widget.setMaximumSize(QtCore.QSize(550, 400))
        self.result_widget.setObjectName("result_widget")
        self.horizontalLayout_2.addWidget(self.result_widget)
        self.verticalLayout_4.addWidget(self.drawing)
        self.applay = QtWidgets.QFrame(self.show)
        self.applay.setMaximumSize(QtCore.QSize(16777215, 80))
        self.applay.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.applay.setFrameShadow(QtWidgets.QFrame.Raised)
        self.applay.setObjectName("applay")
        self.apply = QtWidgets.QPushButton(self.applay)
        self.apply.setGeometry(QtCore.QRect(330, 20, 186, 31))
        self.apply.setObjectName("apply")
        self.but_node = QtWidgets.QSpinBox(self.applay)
        self.but_node.setGeometry(QtCore.QRect(100, 40, 42, 22))
        self.but_node.setObjectName("but_node")
        self.start_node = QtWidgets.QSpinBox(self.applay)
        self.start_node.setGeometry(QtCore.QRect(100, 10, 42, 22))
        self.start_node.setObjectName("start_node")
        self.start_label = QtWidgets.QLabel(self.applay)
        self.start_label.setGeometry(QtCore.QRect(50, 10, 47, 21))
        self.start_label.setToolTip("")
        self.start_label.setObjectName("start_label")
        self.but_label = QtWidgets.QLabel(self.applay)
        self.but_label.setGeometry(QtCore.QRect(50, 40, 47, 21))
        self.but_label.setObjectName("but_label")
        self.verticalLayout_4.addWidget(self.applay)
        self.horizontalLayout.addWidget(self.show)
        self.verticalLayout_5.addWidget(self.mainbody)
        self.footer = QtWidgets.QFrame(self.main)
        self.footer.setMinimumSize(QtCore.QSize(0, 40))
        self.footer.setMaximumSize(QtCore.QSize(16777215, 30))
        self.footer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer.setObjectName("footer")
        self.verticalLayout_5.addWidget(self.footer)
        self.horizontalLayout_7.addWidget(self.main)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.bellmanford.setText(_translate("MainWindow", "Bellman-Ford"))
        self.floydwarchal.setText(_translate("MainWindow", "Floyd-Warchal"))
        self.belmanfordmoore.setText(_translate("MainWindow", "Bellman-ford-Moore"))
        self.fordfulkerson.setText(_translate("MainWindow", "Ford Fulkerson"))
        self.kraskal.setText(_translate("MainWindow", "Kruskal"))
        self.astar.setText(_translate("MainWindow", "A*"))
        self.bfs.setText(_translate("MainWindow", "BFS"))
        self.dfs.setText(_translate("MainWindow", "DFS"))
        self.prefixe.setText(_translate("MainWindow", "Prefixe n-air"))
        self.infixe.setText(_translate("MainWindow", "infixe n-air"))
        self.postfixe.setText(_translate("MainWindow", "postfixe n-air"))
        self.largeur.setText(_translate("MainWindow", "largeur n-air"))
        self.profondeur.setText(_translate("MainWindow", "profondeur n-air"))
        self.nbnode_label.setText(_translate("MainWindow", "nodes number"))
        self.generate_btn.setText(_translate("MainWindow", "Generate"))
        self.arbre.setText(_translate("MainWindow", "Tree"))
        self.graph.setText(_translate("MainWindow", "Graoph"))
        self.apply.setText(_translate("MainWindow", "Apply"))
        self.start_label.setText(_translate("MainWindow", "Start"))
        self.but_label.setText(_translate("MainWindow", "But"))
from initfig import InitFig


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())