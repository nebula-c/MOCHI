import numpy as np

class magnet_parameter():
    def __init__(self,):
        self.mu0 = 4 * np.pi * 1e-7         # Vacuum permeability in T·m/A
        self.tesla_to_gauss = 1e4;        

        self.m_x = 1.0                      # Dipole moment in x-direction (A·m^2)
        self.m_y = 1.0                      # Dipole moment in y-direction (A·m^2)
        self.m_z = 1.0                      # Dipole moment in z-direction (A·m^2)
        self.m = np.array([self.m_x, self.m_y, self.m_z])
        self.N_of_dipole = 100              # Number of dipoles
        self.magnet_length = 20.0           # Magnet length in mm
        
        self.grid_val   = 100               # mm
        self.x_len      = 100               # mm
        self.y_len      = 100               # mm
        self.z_len      = 100               # mm

