import sys
from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt, pyqtSignal,QTimer

from mochi.EventBus import EventBus
from mochi import vec_chart_handler
from mochi import axial_chart_handler
from mochi import setting_handler
from mochi import file_saver
from mochi.internal_parameter import internal_parameter
from mochi.MF_calculator import MF_calculator
from PyQt6.QtWidgets import QDialog, QLabel, QVBoxLayout, QProgressBar


class LoadingDialog(QDialog):
    def __init__(self):
        super().__init__()
        EventBus.subscribe(EventBus.ASK_CALCULATION,self.run)
        # EventBus.subscribe(EventBus.END_CALCULATION,self.close_loading)
        EventBus.subscribe(EventBus.PROGRESS_UPDATE, self.update_progress)
        self.setModal(True)
    
    def run(self):
        self.setWindowTitle("Calculating...")
        layout = QVBoxLayout()
        self.label = QLabel("Running...")
        layout.addWidget(self.label)
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        layout.addWidget(self.progress_bar)
        self.setLayout(layout)
        QTimer.singleShot(0, self.show)

    def update_progress(self, progress, elapsed_time, remaining_time):
        self.progress_bar.setValue(int(progress))
        self.label.setText(f"진행률: {progress:.2f}%\n"
                       f"경과 시간: {elapsed_time:.1f}초\n"
                       f"남은 시간 예상: {remaining_time:.1f}초")

    def close_loading(self):
        self.accept() 


class Mochi_Monitor(QtWidgets.QMainWindow):
    def __init__(self,):
        super().__init__()
        self.axial_chart_handler = axial_chart_handler.axial_chart_handler()
        self.setting_handler = setting_handler.setting_handler()
        self.internal_parameter = internal_parameter
        self.file_saver = file_saver.file_saver()

        self.Basic_Framing()
        self.myLoadingDialog = LoadingDialog()

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
        # self.setting_handler.SetParameters(self.internal_parameter)
        widget_settings = self.setting_handler.widget_settings()
        self.layout.addWidget(widget_settings,stretch=1)
        
        
        
