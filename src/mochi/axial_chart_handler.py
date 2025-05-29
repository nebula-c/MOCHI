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

    def set_xlim(self,xmin,xmax):
        self.ax.set_xlim(xmin, xmax)

    def set_ylim(self,ymin,ymax):
        self.ax.set_ylim(ymin, ymax)

class axial_chart_handler(FigureCanvas):
    def __init__(self,):
        self.x_chart = HeatmapCanvas()
        self.y_chart = HeatmapCanvas()
        self.z_chart = HeatmapCanvas()
    
    def SetParameters(self,parameter_input):
        self.internal_parameter = parameter_input

    def refresh(self):
        x_view_range_max = self.internal_parameter.x_view_range_max
        x_view_range_min = self.internal_parameter.x_view_range_min
        y_view_range_max = self.internal_parameter.y_view_range_max
        y_view_range_min = self.internal_parameter.y_view_range_min
        z_view_range_max = self.internal_parameter.z_view_range_max
        z_view_range_min = self.internal_parameter.z_view_range_min
        
        self.x_chart.set_xlim(x_view_range_min,x_view_range_max)
        self.x_chart.set_ylim(y_view_range_min,y_view_range_max)
        self.y_chart.set_xlim(y_view_range_min,y_view_range_max)
        self.y_chart.set_ylim(z_view_range_min,z_view_range_max)
        self.z_chart.set_xlim(z_view_range_min,z_view_range_max)
        self.z_chart.set_ylim(x_view_range_min,x_view_range_max)

