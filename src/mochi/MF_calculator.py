import numpy as np
import time

from PyQt6.QtCore import QThread

from mochi.EventBus import EventBus
from mochi.internal_parameter import internal_parameter
from mochi.DataStore import DataStore


class MF_calculator:
    def __init__(self,):
        self.run_progress = 0
        self.run_elapsed_time = 0
        self.run_remaining_time = 0
        self.BGND_RUN = self.bgnd_run(self)
        EventBus.subscribe(EventBus.ASK_CALCULATION,self.BGND_RUN.start)

    # def run(self):
    #     self.BGND_RUN = self.bgnd_run(self)
    #     self.BGND_RUN.start()
    
    class bgnd_run(QThread):
        def __init__(self,upper_class_instance):
            super().__init__()
            self.upper_class_instance = upper_class_instance
            self.run_progress = upper_class_instance.run_progress
            self.run_elapsed_time = upper_class_instance.run_elapsed_time
            self.run_remaining_time = upper_class_instance.run_remaining_time
            
        
        def run(self):
            self.get_parameters()
            DataStore.clear()

            magnet_xmin = -self.x_magnet_len/2
            magnet_xmax =  self.x_magnet_len/2
            magnet_ymin = -self.y_magnet_len/2
            magnet_ymax =  self.y_magnet_len/2
            magnet_zmin = -self.z_magnet_len/2
            magnet_zmax =  self.z_magnet_len/2
            dipole_num_y = self.dipole_num_y
            dipole_num_z = self.dipole_num_z
            
            field_resolution =  self.field_resolution

            ### 3D 격자 생성
            x_step = int((self.x_view_range_max-self.x_view_range_min)/field_resolution)
            y_step = int((self.y_view_range_max-self.y_view_range_min)/field_resolution)
            z_step = int((self.z_view_range_max-self.z_view_range_min)/field_resolution)
            x = np.linspace(self.x_view_range_min, self.x_view_range_max, x_step+1)
            y = np.linspace(self.y_view_range_min, self.y_view_range_max, y_step+1)
            z = np.linspace(self.z_view_range_min, self.z_view_range_max, z_step+1)
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
                    
                    # EventBus.emit(EventBus.PROGRESS_UPDATE, progress, elapsed_time, remaining_time)
                    self.upper_class_instance.run_progress = progress
                    self.upper_class_instance.run_elapsed_time = elapsed_time
                    self.upper_class_instance.run_remaining_time = remaining_time
                    
                    
            EventBus.emit(EventBus.END_CALCULATION)

            # end_time = time.time()
            # print("Run time: {:.3f}sec".format(end_time - start_time))


        def get_parameters(self):
            self.mu0          = internal_parameter.mu0
            
            self.B_r          = internal_parameter.B_r
            self.dipole_num_y = int(internal_parameter.dipole_num_y)
            self.dipole_num_z = int(internal_parameter.dipole_num_z)
            
            self.field_resolution = internal_parameter.field_resolution

            self.x_magnet_len = internal_parameter.x_magnet_len
            self.y_magnet_len = internal_parameter.y_magnet_len
            self.z_magnet_len = internal_parameter.z_magnet_len

            self.x_view_range_max = internal_parameter.x_view_range_max
            self.x_view_range_min = internal_parameter.x_view_range_min
            self.y_view_range_max = internal_parameter.y_view_range_max
            self.y_view_range_min = internal_parameter.y_view_range_min
            self.z_view_range_max = internal_parameter.z_view_range_max
            self.z_view_range_min = internal_parameter.z_view_range_min


    





MF_calculator = MF_calculator()
