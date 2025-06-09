from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt, pyqtSignal

# from mochi.EventBus import EventBus
from mochi import vec_chart_handler
from mochi import axial_chart_handler
from mochi import setting_handler
from mochi.internal_parameter import internal_parameter

class Mochi_Monitor(QtWidgets.QMainWindow):
    def __init__(self,):
        super().__init__()
        self.axial_chart_handler = axial_chart_handler.axial_chart_handler()
        self.setting_handler = setting_handler.setting_handler()
        self.internal_parameter = internal_parameter
        signal_setbutton = pyqtSignal()

        self.Basic_Framing()

    def Basic_Framing(self,):
        self.setWindowTitle("MOCHI")
        self.setGeometry(100, 100, 1200, 700)

        self.widget_central = QtWidgets.QWidget()
        self.setCentralWidget(self.widget_central)
        self.layout = QtWidgets.QHBoxLayout(self.widget_central)
        layout_charts = QtWidgets.QVBoxLayout()
        self.widget_central.setStyleSheet("background-color: white;")

        self.layout_chart_up = QtWidgets.QHBoxLayout()
        self.layout_chart_down = QtWidgets.QHBoxLayout()
        layout_charts.addLayout(self.layout_chart_up)
        layout_charts.addLayout(self.layout_chart_down)
        self.layout.addLayout(layout_charts,stretch=5)

        self.vec_chart_handler = vec_chart_handler.vec_chart_handler()
        # self.vec_chart_handler.SetParameters(self.internal_parameter)
        self.vec_chart_handler.SetMagnet()
        self.vec_chart_handler.plot_vector_field()
        self.vec_chart_handler.plot_vector_field()
        self.layout_chart_up.addWidget(self.vec_chart_handler,stretch=1)

        # self.axial_chart_handler.SetParameters(self.internal_parameter)
        self.axial_chart_handler.refresh()
        self.x_chart = self.axial_chart_handler.x_chart
        self.y_chart = self.axial_chart_handler.y_chart
        self.z_chart = self.axial_chart_handler.z_chart
        self.layout_chart_up.addWidget(self.x_chart,stretch=1)
        self.layout_chart_down.addWidget(self.y_chart)
        self.layout_chart_down.addWidget(self.z_chart)


        layout_settings = QtWidgets.QVBoxLayout()
        self.setting_handler.SetParameters(self.internal_parameter)
        widget_settings = self.setting_handler.widget_settings()
        self.layout.addWidget(widget_settings,stretch=1)
        


