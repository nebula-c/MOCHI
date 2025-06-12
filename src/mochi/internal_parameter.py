import numpy as np

class internal_parameter():
    def __init__(self,):
        self.mu0 = 4 * np.pi * 1e-7         # Vacuum permeability in T·m/A

        self.x_magnet_len      = 50               # mm
        self.y_magnet_len      = 5                # mm
        self.z_magnet_len      = 25               # mm

        self.x_view_range_max    = 100           # mm
        self.x_view_range_min    = -100           # mm
        self.y_view_range_max    = 100           # mm
        self.y_view_range_min    = -100           # mm
        self.z_view_range_max    = 100           # mm
        self.z_view_range_min    = -100           # mm

        self.x_3d_range    = 200           # mm
        self.y_3d_range    = 200           # mm
        self.z_3d_range    = 200          # mm
        
        self.B_r        = 14800             # Gauss
        self.dipole_num_y = 10             # count 
        self.dipole_num_z = 10             # count 
        self.field_resolution = 1         # mm


        self.sliceview_x = 0                # mm
        self.sliceview_y = 0                # mm
        self.sliceview_z = 0                # mm


internal_parameter = internal_parameter()