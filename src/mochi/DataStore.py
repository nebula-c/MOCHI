import numpy as np

class DataStore:
    def __init__(self):
        self.vec_r = None
        self.vec_B = None
        self.lenx = None
        self.leny = None
        self.lenz = None

    def set_vec_r(self,inputdata):
        self.vec_r = inputdata
    
    def set_vec_B(self,inputdata):
        self.vec_B = inputdata
    
    def add_vec_B(self,inputdata):
        if self.vec_B is None:
            self.vec_B = np.zeros_like(inputdata)
        self.vec_B += inputdata

    def is_data_fine(self):
        if np.shape(self.vec_r)==np.shape(self.vec_B):
            return True
        else:
            return False
    def set_len_xyz(self,myx,myy,myz):
        self.lenx = myx
        self.leny = myy
        self.lenz = myz
    
    def get_len_xyz(self):
        return self.lenx,self.leny,self.lenz

DataStore = DataStore()