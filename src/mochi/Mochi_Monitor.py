from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt

from mochi import vec_chart_handler
from mochi import axial_chart_handler

class Mochi_Monitor(QtWidgets.QMainWindow):
    def __init__(self,):
        super().__init__()
        self.axial_chart_handler = axial_chart_handler.axial_chart_handler()
        self.Basic_Framing()

    def Basic_Framing(self,):
        self.setWindowTitle("MOCHI")
        self.setGeometry(100, 100, 800, 600)

        self.widget_central = QtWidgets.QWidget()
        self.setCentralWidget(self.widget_central)
        self.layout = QtWidgets.QVBoxLayout(self.widget_central)
        # self.layout.setSpacing(0)
        self.widget_central.setStyleSheet("background-color: white;")

        self.layout_chart_up = QtWidgets.QHBoxLayout(self.widget_central)
        self.layout_chart_down = QtWidgets.QHBoxLayout(self.widget_central)
        self.layout.addLayout(self.layout_chart_up)
        self.layout.addLayout(self.layout_chart_down)

        self.vec_chart_handler = vec_chart_handler.vec_chart_handler()
        self.layout_chart_up.addWidget(self.vec_chart_handler)

        self.x_chart = self.axial_chart_handler.x_chart
        self.y_chart = self.axial_chart_handler.y_chart
        self.z_chart = self.axial_chart_handler.z_chart
        self.layout_chart_up.addWidget(self.x_chart)
        self.layout_chart_down.addWidget(self.y_chart)
        self.layout_chart_down.addWidget(self.z_chart)


