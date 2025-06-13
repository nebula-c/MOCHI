import numpy as np

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

DataStore = DataStore()