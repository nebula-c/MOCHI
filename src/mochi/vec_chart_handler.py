from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

import numpy as np

class vec_chart_handler(FigureCanvas):
    def __init__(self, parent=None):
        fig = Figure()
        super().__init__(fig)
        self.setParent(parent)
        self.ax = fig.add_subplot(111, projection='3d')
        self.plot_vector_field()


    def plot_vector_field(self):
        x, y, z = np.meshgrid(np.arange(-100, 100, 50),
                              np.arange(-100, 100, 50),
                              np.arange(-100, 100, 50))
        u = -y
        v = x
        w = z * 0  # z 성분 0으로 설정

        self.ax.quiver(x, y, z, u, v, w, length=15, normalize=True)
        self.ax.set_xlim([-100,100])
        self.ax.set_ylim([-100,100])
        self.ax.set_zlim([-100,100])

    def SetParameters(self,parameter_input):
        self.x_len = parameter_input.x_len
        self.y_len = parameter_input.y_len
        self.z_len = parameter_input.z_len
        

    def SetMagnet(self,):
        dx = self.x_len
        dy = self.y_len
        dz = self.z_len
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

        box = Poly3DCollection(faces, alpha=0.3, facecolors='cyan', edgecolors='black')
        self.ax.add_collection3d(box)