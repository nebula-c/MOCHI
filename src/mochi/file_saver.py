from PyQt6 import QtWidgets
import numpy as np

from mochi.EventBus import EventBus
from mochi.DataStore import DataStore

class file_saver:
    def __init__(self):
        EventBus.subscribe(EventBus.EXPORT_BUTTON_CLICKED,self.file_export)

    def file_export(self,):
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Save File", "", "Text Files (*.txt);;All Files (*)")
        if file_path:
            vec_r = DataStore.get_vec_r()
            vec_B = DataStore.get_vec_B()
            result_csv = np.hstack((vec_r, vec_B))
            # result_csv_str = np.char.mod('%.3f', result_csv)

            header = "r_x,r_y,r_z,B_x,B_y,B_z"
            np.savetxt(file_path,result_csv,delimiter=",",header=header,comments='', fmt='%.3e')
            # np.savetxt(file_path,result_csv_str,delimiter=",",header=header,comments='', fmt='%s')