import numpy as np
import time

from PyQt6.QtCore import QThread

from mochi.EventBus import EventBus
from mochi.internal_parameter import internal_parameter
from mochi.DataStore import DataStore


class MF_calculator:
    class bgnd_run(QThread):
        def __init__(self,):
            super().__init__()
            
            
        
        def run(self):
            self.get_parameters()

            magnet_xmin = -self.x_magnet_len/2
            magnet_xmax =  self.x_magnet_len/2
            magnet_ymin = -self.y_magnet_len/2
            magnet_ymax =  self.y_magnet_len/2
            magnet_zmin = -self.z_magnet_len/2
            magnet_zmax =  self.z_magnet_len/2
            dipole_num_y = self.dipole_num_y
            dipole_num_z = self.dipole_num_z

            x_3d_range_min = -self.x_3d_range/2
            x_3d_range_max =  self.x_3d_range/2
            y_3d_range_min = -self.y_3d_range/2
            y_3d_range_max =  self.y_3d_range/2
            z_3d_range_min = -self.z_3d_range/2
            z_3d_range_max =  self.z_3d_range/2
            field_resolution =  self.field_resolution

            ### 3D 격자 생성
            x_step = int(x_3d_range_max/field_resolution)
            y_step = int(y_3d_range_max/field_resolution)
            z_step = int(z_3d_range_max/field_resolution)
            x = np.linspace(-x_step*field_resolution, x_step*field_resolution, 2*x_step+1)
            y = np.linspace(-y_step*field_resolution, y_step*field_resolution, 2*y_step+1)
            z = np.linspace(-z_step*field_resolution, z_step*field_resolution, 2*z_step+1)
            X, Y, Z = np.meshgrid(x, y, z, indexing='ij')
            r = np.stack([X, Y, Z], axis=-1)
            r = np.reshape(r,(len(x)*len(y)*len(z),3))
            
            DataStore.set_vec_r(r)
            DataStore.set_len_xyz(len(x),len(y),len(z))


            
            start_time = time.time()
            total_steps = dipole_num_y * dipole_num_z
            current_step = 0

            for y_dipole in np.linspace(magnet_ymin,magnet_ymax,dipole_num_y):
                if dipole_num_y == 1:
                    y_dipole = (magnet_ymin + magnet_ymax)/2
                for z_dipole in np.linspace(magnet_zmin,magnet_zmax,dipole_num_z):
                    if dipole_num_z == 1:
                        z_dipole = (magnet_zmin + magnet_zmax)/2

                    ### Relative coordinate
                    y_rel = y - y_dipole
                    z_rel = z - z_dipole
                    X, Y, Z = np.meshgrid(x, y_rel, z_rel, indexing='ij')

                    r = np.stack([X, Y, Z], axis=-1)
                    r = np.reshape(r,(len(x)*len(y)*len(z),3))
                    np.set_printoptions(threshold=np.inf)
                    
                    r_norm = np.linalg.norm(r, axis=1, keepdims=True)
                    r_norm[r_norm == 0] = np.inf  # 0으로 나눔 방지
                    r_hat = r / r_norm

                    
                    ### dipole moment
                    magnet_V = self.x_magnet_len * self.y_magnet_len * self.z_magnet_len
                    eachamp = (self.B_r * magnet_V / self.mu0) / (dipole_num_y * dipole_num_z)
                    vec_m = eachamp * np.array([1.0, 0.0, 0.0])

                    ### (m · r_hat)
                    m_dot_r = np.dot(r_hat,vec_m)

                    ### B calculation
                    mu0 = self.mu0 
                    B = (mu0/(4*np.pi)) * (3 * m_dot_r[:, np.newaxis]* r_hat - vec_m) / (r_norm ** 3)
        
                    
                    DataStore.add_vec_B(B)


                    current_step += 1
                    current_time = time.time()
                    elapsed_time = current_time - start_time
                    progress = (current_step / total_steps) * 100
                    if progress > 0:
                        estimated_total_time = elapsed_time / (progress / 100)
                        remaining_time = estimated_total_time - elapsed_time
                    else:
                        estimated_total_time = 0
                        remaining_time = 0
                    
                    EventBus.emit(EventBus.PROGRESS_UPDATE, progress, elapsed_time, remaining_time)
                    
            EventBus.emit(EventBus.END_CALCULATION)

            # end_time = time.time()
            # print("Run time: {:.3f}sec".format(end_time - start_time))


        def get_parameters(self):
            self.mu0          = internal_parameter.mu0
            
            self.B_r          = internal_parameter.B_r
            self.dipole_num_y = internal_parameter.dipole_num_y
            self.dipole_num_z = internal_parameter.dipole_num_z
            self.field_resolution = internal_parameter.field_resolution

            self.x_magnet_len = internal_parameter.x_magnet_len
            self.y_magnet_len = internal_parameter.y_magnet_len
            self.z_magnet_len = internal_parameter.z_magnet_len

            self.x_3d_range   = internal_parameter.x_3d_range
            self.y_3d_range   = internal_parameter.y_3d_range
            self.z_3d_range   = internal_parameter.z_3d_range

    def __init__(self,):
        self.BGND_RUN = self.bgnd_run()
        EventBus.subscribe(EventBus.ASK_CALCULATION,self.BGND_RUN.start)





MF_calculator = MF_calculator()
