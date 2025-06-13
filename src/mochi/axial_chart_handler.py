from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.colors import LogNorm
import numpy as np


from mochi.EventBus import EventBus
from mochi.internal_parameter import internal_parameter
from mochi.DataStore import DataStore

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
        self.heatmap = self.ax.imshow(data, cmap='gray', interpolation='None')
        # self.heatmap = self.ax.imshow(data, extent=[-100,100,-100,100], cmap='viridis', interpolation='None')
        self.mycolorbar = self.figure.colorbar(self.heatmap, ax=self.ax)

    def set_xlim(self,xmin,xmax):
        self.ax.set_xlim(xmin, xmax)

    def set_ylim(self,ymin,ymax):
        self.ax.set_ylim(ymin, ymax)

    def set_newextent(self,xmin,xmax,ymin,ymax):
        self.heatmap.set_extent([xmin,xmax,ymin,ymax])


    def set_title(self,mytitle):
        self.ax.set_title(mytitle)

    def set_axis_label(self,xtitle,ytitle):
        self.ax.set_xlabel(xtitle,labelpad=0)
        self.ax.set_ylabel(ytitle,labelpad=0)

    def refresh(self):
        self.ax.set_aspect('auto')
        self.ax.figure.canvas.draw()

    def plot_heatmap(self,data, datarange=None):
        self.mycolorbar.remove()
        self.ax.cla()
        self.heatmap = self.ax.imshow(data, extent=datarange, cmap='viridis', interpolation='None')
        # heatmap = self.ax.imshow(data, norm=LogNorm(), extent=datarange, cmap='viridis', interpolation='None')
        self.mycolorbar = self.figure.colorbar(self.heatmap, ax=self.ax)
        self.heatmap.set_clim(vmin=-100, vmax=100)

        self.refresh()

class axial_chart_handler(FigureCanvas):
    def __init__(self,):
        self.x_chart = HeatmapCanvas()
        self.y_chart = HeatmapCanvas()
        self.z_chart = HeatmapCanvas()

        # self.x_chart.set_title("YZ (X=0)")
        # self.y_chart.set_title("ZX (Y=0)")
        # self.z_chart.set_title("XY (Z=0)")
        self.update_title()
        self.set_labels()

        

        EventBus.subscribe(EventBus.SET_BUTTON_CLICKED,self.refresh)
        EventBus.subscribe(EventBus.SET_BUTTON_CLICKED,self.update_title)
        EventBus.subscribe(EventBus.END_CALCULATION,self.show_data)

    
    def SetParameters(self,parameter_input):
        internal_parameter = parameter_input

    def set_labels(self):
        self.x_chart.set_axis_label("Y","Z")
        self.y_chart.set_axis_label("Z","X")
        self.z_chart.set_axis_label("X","Y")

        self.x_chart.refresh()
        self.y_chart.refresh()
        self.z_chart.refresh()
        


    def refresh(self):
        x_view_range_max = internal_parameter.x_view_range_max
        x_view_range_min = internal_parameter.x_view_range_min
        y_view_range_max = internal_parameter.y_view_range_max
        y_view_range_min = internal_parameter.y_view_range_min
        z_view_range_max = internal_parameter.z_view_range_max
        z_view_range_min = internal_parameter.z_view_range_min
        
        # self.x_chart.set_xlim(y_view_range_min,y_view_range_max)
        # self.x_chart.set_ylim(z_view_range_min,z_view_range_max)
        # self.y_chart.set_xlim(z_view_range_min,z_view_range_max)
        # self.y_chart.set_ylim(x_view_range_min,x_view_range_max)
        # self.z_chart.set_xlim(x_view_range_min,x_view_range_max)
        # self.z_chart.set_ylim(y_view_range_min,y_view_range_max)

        self.x_chart.set_newextent(y_view_range_min,y_view_range_max,z_view_range_min,z_view_range_max)
        self.y_chart.set_newextent(z_view_range_min,z_view_range_max,x_view_range_min,x_view_range_max)
        self.z_chart.set_newextent(x_view_range_min,x_view_range_max,y_view_range_min,y_view_range_max)

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

    def show_data(self):
        my_direction = "B_x"
        # my_direction = "B_y"
        # my_direction = "B_z"

        vec_r = DataStore.get_vec_r()
        vec_B = DataStore.get_vec_B()
        len_x, len_y, len_z = DataStore.get_len_xyz()

        
        Bxyz_XY = []
        Bxyz_YZ = []
        Bxyz_ZX = []

        XY_B = []
        YZ_B = []
        ZX_B = []

        for i in range(len(vec_r)):
            if vec_r[i][0] == 0:
                Bxyz_YZ.append(vec_B[i])
            if vec_r[i][1] == 0:
                Bxyz_ZX.append(vec_B[i])
            if vec_r[i][2] == 0:
                Bxyz_XY.append(vec_B[i])

        Bxyz_YZ = np.array(Bxyz_YZ)
        Bxyz_ZX = np.array(Bxyz_ZX)
        Bxyz_XY = np.array(Bxyz_XY)
        

        if my_direction == "B_x":
            XY_B = Bxyz_XY[:,0]
            YZ_B = Bxyz_YZ[:,0]
            ZX_B = Bxyz_ZX[:,0]
        if my_direction == "B_y":
            XY_B = Bxyz_XY[:,1]
            YZ_B = Bxyz_YZ[:,1]
            ZX_B = Bxyz_ZX[:,1]
        if my_direction == "B_z":
            XY_B = Bxyz_XY[:,2]
            YZ_B = Bxyz_YZ[:,2]
            ZX_B = Bxyz_ZX[:,2]

        XY_B = np.reshape(XY_B,(len_x,len_y)).T
        YZ_B = np.reshape(YZ_B,(len_y,len_z)).T
        ZX_B = np.reshape(ZX_B,(len_x,len_z))


        x_3d_range_min = -internal_parameter.x_3d_range/2
        x_3d_range_max =  internal_parameter.x_3d_range/2
        y_3d_range_min = -internal_parameter.y_3d_range/2
        y_3d_range_max =  internal_parameter.y_3d_range/2
        z_3d_range_min = -internal_parameter.z_3d_range/2
        z_3d_range_max =  internal_parameter.z_3d_range/2

        self.x_chart.plot_heatmap(YZ_B,datarange=[y_3d_range_min,y_3d_range_max,z_3d_range_min,z_3d_range_max])
        self.y_chart.plot_heatmap(ZX_B,datarange=[z_3d_range_min,z_3d_range_max,x_3d_range_min,x_3d_range_max])
        self.z_chart.plot_heatmap(XY_B,datarange=[x_3d_range_min,x_3d_range_max,y_3d_range_min,y_3d_range_max])


        self.set_labels()

