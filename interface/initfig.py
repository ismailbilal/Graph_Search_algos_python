from PyQt5.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvas

from matplotlib.figure import Figure


class InitFig(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.canvas = FigureCanvas(Figure())

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)

        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.canvas.figure.tight_layout()
        self.canvas.axes.set_title("Initial Network")
        self.canvas.axes.axis("off")
        self.setLayout(vertical_layout)
