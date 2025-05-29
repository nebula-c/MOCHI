from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np


class HeatmapCanvas(FigureCanvas):
    def __init__(self, parent=None):
        fig = Figure()
        super().__init__(fig)
        self.ax = fig.add_subplot(111)
        self.plot_test_heatmap()

    def plot_test_heatmap(self):
        data = np.random.rand(100, 100)
        heatmap = self.ax.imshow(data, cmap='viridis', interpolation='None')
        self.figure.colorbar(heatmap, ax=self.ax)


class axial_chart_handler(FigureCanvas):
    def __init__(self,):
        self.x_chart = HeatmapCanvas()
        self.y_chart = HeatmapCanvas()
        self.z_chart = HeatmapCanvas()
    


