import numpy as np
from mochi.internal_parameter import internal_parameter

class DataStore:
    def __init__(self):
        self.__vec_r = None
        self.__vec_B = None
        self.__lenx = None
        self.__leny = None
        self.__lenz = None

    def set_vec_r(self,inputdata):
        self.__vec_r = inputdata
    
    def set_vec_B(self,inputdata):
        self.__vec_B = inputdata
    
    def add_vec_B(self,inputdata):
        if self.__vec_B is None:
            self.__vec_B = np.zeros_like(inputdata)
        self.__vec_B += inputdata

    def get_vec_B(self,):
        self.blank_magnet()
        return self.__vec_B
    
    def get_vec_r(self,):
        return self.__vec_r

    def is_data_fine(self):
        if np.shape(self.__vec_r)==np.shape(self.__vec_B):
            return True
        else:
            return False
    
    def set_len_xyz(self,myx,myy,myz):
        self.__lenx = myx
        self.__leny = myy
        self.__lenz = myz
    
    def get_len_xyz(self):
        return self.__lenx,self.__leny,self.__lenz

    def clear(self):
        self.__vec_r = None
        self.__vec_B = None
        self.__lenx = None
        self.__leny = None
        self.__lenz = None

    def blank_magnet(self):
        if not self.is_data_fine:
            return
        
        for i in range (np.shape(self.__vec_B)[0]):
            my_vec_B = self.__vec_B[i]
            my_vec_r = self.__vec_r[i]

            x = my_vec_r[0]
            y = my_vec_r[1]
            z = my_vec_r[2]

            if (abs(x) < internal_parameter.x_magnet_len/2) and (abs(y) < internal_parameter.y_magnet_len/2) and (abs(z) < internal_parameter.z_magnet_len/2):
                self.__vec_B[i][0] = None
                self.__vec_B[i][1] = None
                self.__vec_B[i][2] = None
    



DataStore = DataStore()