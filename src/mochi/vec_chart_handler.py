from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

class vec_chart_handler(FigureCanvas):
    def __init__(self, parent=None):
        fig = Figure()
        super().__init__(fig)
        self.setParent(parent)
        self.ax = fig.add_subplot(111, projection='3d')
        self.plot_vector_field()


    def plot_vector_field(self):
        x, y, z = np.meshgrid(np.arange(-1, 1, 0.5),
                              np.arange(-1, 1, 0.5),
                              np.arange(-1, 1, 0.5))
        u = -y
        v = x
        w = z * 0  # z 성분 0으로 설정

        self.ax.quiver(x, y, z, u, v, w, length=0.1, normalize=True)
        self.ax.set_xlim([-1,1])
        self.ax.set_ylim([-1,1])
        self.ax.set_zlim([-1,1])
