from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

from mochi.EventBus import EventBus
from mochi.internal_parameter import internal_parameter

class HeatmapCanvas(FigureCanvas):
    def __init__(self, parent=None):
        fig = Figure()
        super().__init__(fig)
        self.ax = fig.add_subplot(111)
        self.plot_test_heatmap()
        self.ax.set_aspect('equal')
        self.setMinimumSize(300, 300)

    def plot_test_heatmap(self):
        data = np.random.rand(100, 100)
        heatmap = self.ax.imshow(data, cmap='viridis', interpolation='None')
        self.figure.colorbar(heatmap, ax=self.ax)

    def set_xlim(self,xmin,xmax):
        self.ax.set_xlim(xmin, xmax)

    def set_ylim(self,ymin,ymax):
        self.ax.set_ylim(ymin, ymax)

    def set_title(self,mytitle):
        self.ax.set_title(mytitle)

    def set_axis_label(self,xtitle,ytitle):
        self.ax.set_xlabel(xtitle,labelpad=0)
        self.ax.set_ylabel(ytitle,labelpad=0)

    def refresh(self):
        self.ax.set_aspect('equal')
        self.ax.figure.canvas.draw()

class axial_chart_handler(FigureCanvas):
    def __init__(self,):
        self.x_chart = HeatmapCanvas()
        self.y_chart = HeatmapCanvas()
        self.z_chart = HeatmapCanvas()

        # self.x_chart.set_title("YZ (X=0)")
        # self.y_chart.set_title("ZX (Y=0)")
        # self.z_chart.set_title("XY (Z=0)")
        self.update_title()

        self.x_chart.set_axis_label("Y","Z")
        self.y_chart.set_axis_label("Z","X")
        self.z_chart.set_axis_label("X","Y")

        EventBus.subscribe(EventBus.SET_BUTTON_CLICKED,self.refresh)
        EventBus.subscribe(EventBus.SET_BUTTON_CLICKED,self.update_title)

    
    def SetParameters(self,parameter_input):
        internal_parameter = parameter_input

    def refresh(self):
        x_view_range_max = internal_parameter.x_view_range_max
        x_view_range_min = internal_parameter.x_view_range_min
        y_view_range_max = internal_parameter.y_view_range_max
        y_view_range_min = internal_parameter.y_view_range_min
        z_view_range_max = internal_parameter.z_view_range_max
        z_view_range_min = internal_parameter.z_view_range_min
        
        self.x_chart.set_xlim(y_view_range_min,y_view_range_max)
        self.x_chart.set_ylim(z_view_range_min,z_view_range_max)
        self.y_chart.set_xlim(z_view_range_min,z_view_range_max)
        self.y_chart.set_ylim(x_view_range_min,x_view_range_max)
        self.z_chart.set_xlim(x_view_range_min,x_view_range_max)
        self.z_chart.set_ylim(y_view_range_min,y_view_range_max)

        self.x_chart.refresh()
        self.y_chart.refresh()
        self.z_chart.refresh()

    def update_title(self):
        self.x_chart.set_title("YZ (X={})".format(internal_parameter.sliceview_x))
        self.y_chart.set_title("ZX (Y={})".format(internal_parameter.sliceview_y))
        self.z_chart.set_title("XY (Z={})".format(internal_parameter.sliceview_z))

        self.x_chart.refresh()
        self.y_chart.refresh()
        self.z_chart.refresh()

