import numpy as np

class internal_parameter():
    def __init__(self,):
        self.mu0 = 4 * np.pi * 1e-7         # Vacuum permeability in T·m/A

        self.x_magnet_len      = 5                # mm
        self.y_magnet_len      = 50               # mm
        self.z_magnet_len      = 25               # mm
        self.B_r        = 14800             # Gauss
        self.dipole_num_y = 10             # count 
        self.dipole_num_z = 10             # count 

        self.x_view_range_max    = 100           # mm
        self.x_view_range_min    = -100           # mm
        self.y_view_range_max    = 100           # mm
        self.y_view_range_min    = -100           # mm
        self.z_view_range_max    = 100           # mm
        self.z_view_range_min    = -100           # mm
        self.field_resolution = 10         # mm

        self.sliceview_x = 0                # mm
        self.sliceview_y = 0                # mm
        self.sliceview_z = 0                # mm
        self.target_direction = "B_x"

        self.YZ_lim_max =  100
        self.YZ_lim_min = -100
        self.ZX_lim_max =  100
        self.ZX_lim_min = -100
        self.XY_lim_max =  100
        self.XY_lim_min = -100

internal_parameter = internal_parameter()