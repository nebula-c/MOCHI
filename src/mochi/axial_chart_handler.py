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
        self.ax.set_ylabel(ytitle,labelpad=-10)

    def refresh(self):
        self.ax.set_aspect('auto')
        self.ax.figure.canvas.draw()

    def plot_heatmap(self,data, datarange=None):
        self.mycolorbar.remove()
        self.ax.cla()
        self.heatmap = self.ax.imshow(data, extent=datarange, cmap='viridis', interpolation='None',origin='lower')
        # heatmap = self.ax.imshow(data, norm=LogNorm(), extent=datarange, cmap='viridis', interpolation='None')
        self.mycolorbar = self.figure.colorbar(self.heatmap, ax=self.ax)
        self.heatmap.set_clim(vmin=-100, vmax=100)
        self.mycolorbar.set_label("Gauss (Max: 100G)",rotation=270)

        self.refresh()

class axial_chart_handler(FigureCanvas):
    def __init__(self,):
        self.x_chart = HeatmapCanvas()
        self.y_chart = HeatmapCanvas()
        self.z_chart = HeatmapCanvas()

        self.get_parameters()

        # self.x_chart.set_title("YZ (X=0)")
        # self.y_chart.set_title("ZX (Y=0)")
        # self.z_chart.set_title("XY (Z=0)")
        self.update_title()
        self.set_labels()

        

        EventBus.subscribe(EventBus.SET_BUTTON_CLICKED,self.refresh)
        EventBus.subscribe(EventBus.SET_BUTTON_CLICKED,self.update_title)
        EventBus.subscribe(EventBus.SHOW_PLOT,self.show_data)

    def get_parameters(self):
        self.x_view_range_max = internal_parameter.x_view_range_max
        self.x_view_range_min = internal_parameter.x_view_range_min
        self.y_view_range_max = internal_parameter.y_view_range_max
        self.y_view_range_min = internal_parameter.y_view_range_min
        self.z_view_range_max = internal_parameter.z_view_range_max
        self.z_view_range_min = internal_parameter.z_view_range_min

    def set_labels(self):
        self.x_chart.set_axis_label("Y(mm)","Z(mm)")
        self.y_chart.set_axis_label("Z(mm)","X(mm)")
        self.z_chart.set_axis_label("X(mm)","Y(mm)")

        self.x_chart.refresh()
        self.y_chart.refresh()
        self.z_chart.refresh()
        


    def refresh(self):
        # self.x_chart.set_xlim(y_view_range_min,y_view_range_max)
        # self.x_chart.set_ylim(z_view_range_min,z_view_range_max)
        # self.y_chart.set_xlim(z_view_range_min,z_view_range_max)
        # self.y_chart.set_ylim(x_view_range_min,x_view_range_max)
        # self.z_chart.set_xlim(x_view_range_min,x_view_range_max)
        # self.z_chart.set_ylim(y_view_range_min,y_view_range_max)
        self.get_parameters()

        self.x_chart.set_newextent(self.y_view_range_min,self.y_view_range_max,self.z_view_range_min,self.z_view_range_max)
        self.y_chart.set_newextent(self.z_view_range_min,self.z_view_range_max,self.x_view_range_min,self.x_view_range_max)
        self.z_chart.set_newextent(self.x_view_range_min,self.x_view_range_max,self.y_view_range_min,self.y_view_range_max)

        self.x_chart.refresh()
        self.y_chart.refresh()
        self.z_chart.refresh()

    def update_title(self):
        self.x_chart.set_title("{} @ plane_YZ(X={} mm)".format(internal_parameter.target_direction,internal_parameter.sliceview_x))
        self.y_chart.set_title("{} @ plane_ZX(Y={} mm)".format(internal_parameter.target_direction,internal_parameter.sliceview_y))
        self.z_chart.set_title("{} @ plane_XY(Z={} mm)".format(internal_parameter.target_direction,internal_parameter.sliceview_z))

        self.x_chart.refresh()
        self.y_chart.refresh()
        self.z_chart.refresh()

    def show_data(self):
        my_direction = internal_parameter.target_direction
        # my_direction = "B_x"
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

        target_plane_X = internal_parameter.sliceview_x
        target_plane_Y = internal_parameter.sliceview_y
        target_plane_Z = internal_parameter.sliceview_z


        x_step = int((internal_parameter.x_view_range_max-internal_parameter.x_view_range_min)/internal_parameter.field_resolution)
        y_step = int((internal_parameter.y_view_range_max-internal_parameter.y_view_range_min)/internal_parameter.field_resolution)
        z_step = int((internal_parameter.z_view_range_max-internal_parameter.z_view_range_min)/internal_parameter.field_resolution)
        x_lattice = np.linspace(internal_parameter.x_view_range_min, internal_parameter.x_view_range_max, x_step+1)
        y_lattice = np.linspace(internal_parameter.y_view_range_min, internal_parameter.y_view_range_max, y_step+1)
        z_lattice = np.linspace(internal_parameter.z_view_range_min, internal_parameter.z_view_range_max, z_step+1)
        
        if target_plane_X in x_lattice : is_get_YZ = True
        else : is_get_YZ = False
        if target_plane_Y in y_lattice : is_get_ZX = True
        else : is_get_ZX = False
        if target_plane_Z in z_lattice : is_get_XY = True
        else : is_get_XY = False

        for i in range(len(vec_r)):
            if(is_get_YZ):
                if vec_r[i][0] == target_plane_X:
                    Bxyz_YZ.append(vec_B[i])
            if(is_get_ZX):
                if vec_r[i][1] == target_plane_Y:
                    Bxyz_ZX.append(vec_B[i])
            if(is_get_XY):
                if vec_r[i][2] == target_plane_Z:
                    Bxyz_XY.append(vec_B[i])

        Bxyz_YZ = np.array(Bxyz_YZ)
        Bxyz_ZX = np.array(Bxyz_ZX)
        Bxyz_XY = np.array(Bxyz_XY)
        

        if my_direction == "B_x":
            if(is_get_XY): XY_B = Bxyz_XY[:,0]
            if(is_get_YZ): YZ_B = Bxyz_YZ[:,0]
            if(is_get_ZX): ZX_B = Bxyz_ZX[:,0]
        if my_direction == "B_y":
            if(is_get_XY): XY_B = Bxyz_XY[:,1]
            if(is_get_YZ): YZ_B = Bxyz_YZ[:,1]
            if(is_get_ZX): ZX_B = Bxyz_ZX[:,1]
        if my_direction == "B_z":
            if(is_get_XY): XY_B = Bxyz_XY[:,2]
            if(is_get_YZ): YZ_B = Bxyz_YZ[:,2]
            if(is_get_ZX): ZX_B = Bxyz_ZX[:,2]

        if(is_get_XY): XY_B = np.reshape(XY_B,(len_x,len_y)).T
        if(is_get_YZ): YZ_B = np.reshape(YZ_B,(len_y,len_z)).T
        if(is_get_ZX): ZX_B = np.reshape(ZX_B,(len_x,len_z))


        # x_3d_range_min = -internal_parameter.x_3d_range/2
        # x_3d_range_max =  internal_parameter.x_3d_range/2
        # y_3d_range_min = -internal_parameter.y_3d_range/2
        # y_3d_range_max =  internal_parameter.y_3d_range/2
        # z_3d_range_min = -internal_parameter.z_3d_range/2
        # z_3d_range_max =  internal_parameter.z_3d_range/2

        # self.x_chart.plot_heatmap(YZ_B,datarange=[y_3d_range_min,y_3d_range_max,z_3d_range_min,z_3d_range_max])
        # self.y_chart.plot_heatmap(ZX_B,datarange=[z_3d_range_min,z_3d_range_max,x_3d_range_min,x_3d_range_max])
        # self.z_chart.plot_heatmap(XY_B,datarange=[x_3d_range_min,x_3d_range_max,y_3d_range_min,y_3d_range_max])



        if(is_get_YZ): self.x_chart.plot_heatmap(YZ_B,datarange=[self.y_view_range_min,self.y_view_range_max,self.z_view_range_min,self.z_view_range_max])
        if(is_get_ZX): self.y_chart.plot_heatmap(ZX_B,datarange=[self.z_view_range_min,self.z_view_range_max,self.x_view_range_min,self.x_view_range_max])
        if(is_get_XY): self.z_chart.plot_heatmap(XY_B,datarange=[self.x_view_range_min,self.x_view_range_max,self.y_view_range_min,self.y_view_range_max])

        self.refresh()
        self.set_labels()
        self.update_title()

