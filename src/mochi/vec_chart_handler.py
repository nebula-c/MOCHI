from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

import numpy as np
from mochi.EventBus import EventBus
from mochi.internal_parameter import internal_parameter

class vec_chart_handler(FigureCanvas):
    def __init__(self, parent=None):
        fig = Figure()
        super().__init__(fig)
        self.setParent(parent)
        self.magnet_box = None
        self.ax = fig.add_subplot(111, projection='3d')
        self.ax.set_xlabel('X',labelpad=0)
        self.ax.set_ylabel('Y',labelpad=0)
        self.ax.set_zlabel('Z',labelpad=0)
        self.setMinimumSize(300, 300)

        EventBus.subscribe(EventBus.SET_BUTTON_CLICKED,self.set_range)
        EventBus.subscribe(EventBus.SET_BUTTON_CLICKED,self.SetMagnet)


    def plot_vector_field(self):
        # y_temp = np.linspace(-internal_parameter.y_magnet_len/2,internal_parameter.y_magnet_len/2,internal_parameter.dipole_num_y)
        # z_temp = np.linspace(-internal_parameter.z_magnet_len/2,internal_parameter.z_magnet_len/2,internal_parameter.dipole_num_z)
        # x_temp = np.zeros_like(y_temp)

        # x,y,z = np.meshgrid(x_temp,y_temp,z_temp)
        # u = 1; v = 0; w = 0


        # x, y, z = np.meshgrid(np.arange(-100, 100, 50),
        #                       np.arange(-100, 100, 50),
        #                       np.arange(-100, 100, 50))
        # u = -y
        # v = x
        # w = z * 0
        # self.ax.quiver(x, y, z, u, v, w, length=15, normalize=True)

        self.ax.quiver(0,0,0, 1,0,0, length=30, normalize=True)
        # self.ax.set_xlim([-internal_parameter.x_3d_range/2,internal_parameter.x_3d_range/2])
        # self.ax.set_ylim([-internal_parameter.y_3d_range/2,internal_parameter.y_3d_range/2])
        # self.ax.set_zlim([-internal_parameter.z_3d_range/2,internal_parameter.z_3d_range/2])

        self.ax.set_xlim([internal_parameter.x_view_range_min,internal_parameter.x_view_range_max])
        self.ax.set_ylim([internal_parameter.y_view_range_min,internal_parameter.y_view_range_max])
        self.ax.set_zlim([internal_parameter.z_view_range_min,internal_parameter.z_view_range_max])

    def set_range(self):
        # self.ax.set_xlim([-internal_parameter.x_3d_range/2,internal_parameter.x_3d_range/2])
        # self.ax.set_ylim([-internal_parameter.y_3d_range/2,internal_parameter.y_3d_range/2])
        # self.ax.set_zlim([-internal_parameter.z_3d_range/2,internal_parameter.z_3d_range/2])
        self.ax.set_xlim([internal_parameter.x_view_range_min,internal_parameter.x_view_range_max])
        self.ax.set_ylim([internal_parameter.y_view_range_min,internal_parameter.y_view_range_max])
        self.ax.set_zlim([internal_parameter.z_view_range_min,internal_parameter.z_view_range_max])
        self.ax.figure.canvas.draw()

    def SetParameters(self,parameter_input):
        internal_parameter = parameter_input
        

    def SetMagnet(self,):
        if self.magnet_box is not None:
            self.magnet_box.remove()
        dx = internal_parameter.x_magnet_len
        dy = internal_parameter.y_magnet_len
        dz = internal_parameter.z_magnet_len
        x = 0 - dx/2
        y = 0 - dy/2
        z = 0 - dz/2

        vertices = np.array([
            [x, y, z],
            [x + dx, y, z],
            [x + dx, y + dy, z],
            [x, y + dy, z],
            [x, y, z + dz],
            [x + dx, y, z + dz],
            [x + dx, y + dy, z + dz],
            [x, y + dy, z + dz]
        ])

        faces = [
            [vertices[j] for j in [0, 1, 2, 3]],
            [vertices[j] for j in [4, 5, 6, 7]],
            [vertices[j] for j in [0, 1, 5, 4]],
            [vertices[j] for j in [2, 3, 7, 6]],
            [vertices[j] for j in [1, 2, 6, 5]],
            [vertices[j] for j in [4, 7, 3, 0]]
        ]

        self.magnet_box = Poly3DCollection(faces, alpha=0.3, facecolors='grey', edgecolors='black')
        self.ax.add_collection3d(self.magnet_box)

    def refresh(self):
        self.SetMagnet()
        