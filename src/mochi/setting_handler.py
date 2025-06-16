from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt, pyqtSignal
import numpy as np

from mochi.EventBus import EventBus
from mochi.internal_parameter import internal_parameter


class setting_handler:
    def __init__(self):
        EventBus.subscribe(EventBus.END_CALCULATION,self.update_xyz_plane_combobox)

    def widget_settings(self,):
        self.widget_3d_range = self.build_widget_3d_range()
        self.widget_view_range = self.build_widget_view_range()
        self.widget_magnet_val = self.build_widget_magnet_val()
        self.widget_view = self.build_widget_view()
        self.widget_dipole_num = self.build_widget_dipole_num()
        
        layout_settings = QtWidgets.QVBoxLayout()
        layout_buttons = QtWidgets.QHBoxLayout()
        layout_buttons2 = QtWidgets.QHBoxLayout()

        widget_magnet_val = self.widget_magnet_val
        widget_magnet_val.setContentsMargins(0, 0, 0, 0)
        layout_settings.addWidget(widget_magnet_val)
        
        line1 = self.set_dot_line()
        layout_settings.addWidget(line1)
        layout_settings.addStretch()
        
        widget_3d_range = self.widget_3d_range
        widget_3d_range.setContentsMargins(0, 0, 0, 0)
        layout_settings.addWidget(widget_3d_range)


        line2 = self.set_dot_line()
        layout_settings.addWidget(line2)
        layout_settings.addStretch()

        widget_dipole_num = self.widget_dipole_num
        widget_dipole_num.setContentsMargins(0, 0, 0, 0)
        layout_settings.addWidget(widget_dipole_num)

        line3 = self.set_dot_line()
        layout_settings.addWidget(line3)
        layout_settings.addStretch()
        
        widget_view_range = self.widget_view_range
        widget_view_range.setContentsMargins(0, 0, 0, 0)
        layout_settings.addWidget(widget_view_range)

        set_buttons = self.set_buttons()
        run_buttons = self.run_buttons()
        export_buttons = self.export_buttons()
        layout_buttons.addWidget(set_buttons)
        layout_buttons.addWidget(run_buttons)
        layout_buttons.addWidget(export_buttons)
        layout_buttons.setContentsMargins(0, 0, 0, 0)
        layout_settings.addLayout(layout_buttons)

        line4 = self.set_line()
        layout_settings.addWidget(line4)
        layout_settings.addStretch()


        widget_view = self.widget_view
        widget_view.setContentsMargins(0, 0, 0, 0)
        layout_settings.addWidget(widget_view)

        view_buttons = self.view_buttons()
        # export_buttons = self.export_buttons()
        layout_buttons2.addWidget(view_buttons)
        # layout_buttons2.addWidget(export_buttons)
        layout_settings.addLayout(layout_buttons2)

        widget_temp_setting = QtWidgets.QWidget()        
        widget_temp_setting.setLayout(layout_settings)
        return widget_temp_setting

    def build_widget_3d_range(self,):
        label_title_range      = QtWidgets.QLabel("3D range (mm)")
        
        layout_range = QtWidgets.QVBoxLayout()
        layout_range_val = QtWidgets.QHBoxLayout()
        layout_3d_xrange = QtWidgets.QHBoxLayout()
        layout_3d_yrange = QtWidgets.QHBoxLayout()
        layout_3d_zrange = QtWidgets.QHBoxLayout()
        

        label_xmax      = QtWidgets.QLabel("X")
        self.lineedit_3d_xrange   = QtWidgets.QLineEdit("{}".format(internal_parameter.x_3d_range))
        lineedit_3d_xrange = self.lineedit_3d_xrange
        layout_3d_xrange.addWidget(label_xmax   )
        layout_3d_xrange.addWidget(lineedit_3d_xrange)

        label_ymax      = QtWidgets.QLabel("Y")
        self.lineedit_3d_yrange   = QtWidgets.QLineEdit("{}".format(internal_parameter.y_3d_range))
        lineedit_3d_yrange = self.lineedit_3d_yrange
        layout_3d_yrange.addWidget(label_ymax   )
        layout_3d_yrange.addWidget(lineedit_3d_yrange)

        label_zmax      = QtWidgets.QLabel("Z")
        self.lineedit_3d_zrange   = QtWidgets.QLineEdit("{}".format(internal_parameter.z_3d_range))
        lineedit_3d_zrange = self.lineedit_3d_zrange
        layout_3d_zrange.addWidget(label_zmax   )
        layout_3d_zrange.addWidget(lineedit_3d_zrange)
        

        layout_range.addWidget(label_title_range,stretch=1)
        layout_range_val.addLayout(layout_3d_xrange,stretch=1)
        layout_range_val.addLayout(layout_3d_yrange,stretch=1)
        layout_range_val.addLayout(layout_3d_zrange,stretch=1)
        layout_range.addLayout(layout_range_val)

        widget_temp_range = QtWidgets.QWidget()        
        widget_temp_range.setLayout(layout_range)
        return widget_temp_range


    def build_widget_view_range(self,):
        label_title_range      = QtWidgets.QLabel("View range")
        
        layout_range = QtWidgets.QVBoxLayout()
        layout_range_val = QtWidgets.QVBoxLayout()
        layout_x_len = QtWidgets.QHBoxLayout()
        layout_y_len = QtWidgets.QHBoxLayout()
        layout_z_len = QtWidgets.QHBoxLayout()
        layout_field_resol = QtWidgets.QHBoxLayout()

        label_xmin      = QtWidgets.QLabel("xmin")
        self.lineedit_xmin   = QtWidgets.QLineEdit("{}".format(internal_parameter.x_view_range_min))
        lineedit_xmin = self.lineedit_xmin
        label_xmax      = QtWidgets.QLabel("xmax")
        self.lineedit_xmax   = QtWidgets.QLineEdit("{}".format(internal_parameter.x_view_range_max))
        lineedit_xmax = self.lineedit_xmax
        layout_x_len.addWidget(label_xmin   )
        layout_x_len.addWidget(lineedit_xmin)
        layout_x_len.addWidget(label_xmax   )
        layout_x_len.addWidget(lineedit_xmax)

        label_ymin      = QtWidgets.QLabel("ymin")
        self.lineedit_ymin   = QtWidgets.QLineEdit("{}".format(internal_parameter.y_view_range_min))
        lineedit_ymin = self.lineedit_ymin
        label_ymax      = QtWidgets.QLabel("ymax")
        self.lineedit_ymax   = QtWidgets.QLineEdit("{}".format(internal_parameter.y_view_range_max))
        lineedit_ymax = self.lineedit_ymax
        layout_y_len.addWidget(label_ymin   )
        layout_y_len.addWidget(lineedit_ymin)
        layout_y_len.addWidget(label_ymax   )
        layout_y_len.addWidget(lineedit_ymax)

        label_zmin      = QtWidgets.QLabel("zmin")
        self.lineedit_zmin   = QtWidgets.QLineEdit("{}".format(internal_parameter.z_view_range_min))
        lineedit_zmin = self.lineedit_zmin
        label_zmax      = QtWidgets.QLabel("zmax")
        self.lineedit_zmax   = QtWidgets.QLineEdit("{}".format(internal_parameter.z_view_range_max))
        lineedit_zmax = self.lineedit_zmax
        layout_z_len.addWidget(label_zmin   )
        layout_z_len.addWidget(lineedit_zmin)
        layout_z_len.addWidget(label_zmax   )
        layout_z_len.addWidget(lineedit_zmax)

        label_field_resol   = QtWidgets.QLabel("Field resolution(mm)")
        lineedit_field_resol= QtWidgets.QLineEdit("{}".format(internal_parameter.x_magnet_len))
        self.lineedit_field_resol  =   lineedit_field_resol
        layout_field_resol.addWidget(label_field_resol   )
        layout_field_resol.addWidget(lineedit_field_resol)

        layout_range.addWidget(label_title_range,stretch=1)
        layout_range_val.addLayout(layout_x_len,stretch=1)
        layout_range_val.addLayout(layout_y_len,stretch=1)
        layout_range_val.addLayout(layout_z_len,stretch=1)
        layout_range_val.addLayout(layout_field_resol,stretch=1)
        layout_range.addLayout(layout_range_val)

        widget_temp_range = QtWidgets.QWidget()        
        widget_temp_range.setLayout(layout_range)
        return widget_temp_range


    def build_widget_magnet_val(self,):
        label_title_range      = QtWidgets.QLabel("Magnet setting")
        
        layout_magnet = QtWidgets.QVBoxLayout()
        layout_val_1 = QtWidgets.QHBoxLayout()
        layout_magnet_val_2 = QtWidgets.QHBoxLayout()
        layout_x_len = QtWidgets.QHBoxLayout()
        layout_y_len = QtWidgets.QHBoxLayout()
        layout_z_len = QtWidgets.QHBoxLayout()
        layout_br = QtWidgets.QHBoxLayout()
        
        label_xlen      = QtWidgets.QLabel("x length")
        lineedit_magnet_xlen   = QtWidgets.QLineEdit("{}".format(internal_parameter.x_magnet_len))
        self.lineedit_magnet_xlen  =   lineedit_magnet_xlen
        layout_x_len.addWidget(label_xlen   )
        layout_x_len.addWidget(lineedit_magnet_xlen)

        label_ylen      = QtWidgets.QLabel("y length")
        lineedit_magnet_ylen   = QtWidgets.QLineEdit("{}".format(internal_parameter.y_magnet_len))
        self.lineedit_magnet_ylen  =   lineedit_magnet_ylen
        layout_y_len.addWidget(label_ylen   )
        layout_y_len.addWidget(lineedit_magnet_ylen)

        label_zlen      = QtWidgets.QLabel("z length")
        lineedit_magnet_zlen   = QtWidgets.QLineEdit("{}".format(internal_parameter.z_magnet_len))
        self.lineedit_magnet_zlen  =   lineedit_magnet_zlen
        layout_z_len.addWidget(label_zlen   )
        layout_z_len.addWidget(lineedit_magnet_zlen)

        label_br      = QtWidgets.QLabel("B_r")
        lineedit_br   = QtWidgets.QLineEdit("{}".format(internal_parameter.B_r))
        self.lineedit_br = lineedit_br
        layout_br.addWidget(label_br   )
        layout_br.addWidget(lineedit_br)
        
        layout_magnet.addWidget(label_title_range)
        layout_val_1.addLayout(layout_x_len,stretch=1)
        layout_val_1.addLayout(layout_y_len,stretch=1)
        layout_magnet_val_2.addLayout(layout_z_len,stretch=1)
        layout_magnet_val_2.addLayout(layout_br,stretch=1)
        layout_magnet.addLayout(layout_val_1)
        layout_magnet.addLayout(layout_magnet_val_2)
        
        widget_temp_magnet = QtWidgets.QWidget()        
        widget_temp_magnet.setLayout(layout_magnet)
        return widget_temp_magnet


    def build_widget_dipole_num(self,):
        layout_dipole_num = QtWidgets.QVBoxLayout()
        layout_val_1 = QtWidgets.QHBoxLayout()
        layout_x_dipole = QtWidgets.QHBoxLayout()
        layout_y_dipole = QtWidgets.QHBoxLayout()
        layout_br = QtWidgets.QHBoxLayout()
        
        label_section_title    = QtWidgets.QLabel("Number of dipoles")
        label_xdipole   = QtWidgets.QLabel("X-axis")
        lineedit_xdipole= QtWidgets.QLineEdit("{}".format(internal_parameter.x_magnet_len))
        self.lineedit_xdipole  =   lineedit_xdipole
        layout_x_dipole.addWidget(label_xdipole   )
        layout_x_dipole.addWidget(lineedit_xdipole)

        label_ydipole   = QtWidgets.QLabel("Y-axis")
        lineedit_ydipole= QtWidgets.QLineEdit("{}".format(internal_parameter.x_magnet_len))
        self.lineedit_ydipole  =   lineedit_ydipole
        layout_y_dipole.addWidget(label_ydipole   )
        layout_y_dipole.addWidget(lineedit_ydipole)
        
        layout_dipole_num.addWidget(label_section_title)
        layout_val_1.addLayout(layout_x_dipole,stretch=1)
        layout_val_1.addLayout(layout_y_dipole,stretch=1)
        layout_dipole_num.addLayout(layout_val_1)
        
        widget_temp_dipole_num = QtWidgets.QWidget()        
        widget_temp_dipole_num.setLayout(layout_dipole_num)
        return widget_temp_dipole_num


    def build_widget_view(self,):
        label_title_view      = QtWidgets.QLabel("View setting")
        

        layout_view = QtWidgets.QVBoxLayout()
        layout_range_val = QtWidgets.QHBoxLayout()
        layout_view_val_1 = QtWidgets.QVBoxLayout()
        layout_view_val_2 = QtWidgets.QVBoxLayout()

        label_x_equal      = QtWidgets.QLabel("x = ")
        label_y_equal      = QtWidgets.QLabel("y = ")
        label_z_equal      = QtWidgets.QLabel("z = ")

        layout_view_val_1.addWidget(label_x_equal)
        layout_view_val_1.addWidget(label_y_equal)
        layout_view_val_1.addWidget(label_z_equal)

        self.combomox_x_lattice = QtWidgets.QComboBox()
        self.combomox_y_lattice = QtWidgets.QComboBox()
        self.combomox_z_lattice = QtWidgets.QComboBox()

        self.combomox_x_lattice.setStyleSheet("""
            QComboBox {
                background-color: white;
                color: black;
                border: 1px solid gray;
                padding: 2px;
            }
        """)
        self.combomox_y_lattice.setStyleSheet("""
            QComboBox {
                background-color: white;
                color: black;
                border: 1px solid gray;
                padding: 2px;
            }
        """)
        self.combomox_z_lattice.setStyleSheet("""
            QComboBox {
                background-color: white;
                color: black;
                border: 1px solid gray;
                padding: 2px;
            }
        """)
        
        self.combomox_x_lattice.addItems(['0'])
        self.combomox_y_lattice.addItems(['0'])
        self.combomox_z_lattice.addItems(['0'])

        layout_view_val_2.addWidget(self.combomox_x_lattice)
        layout_view_val_2.addWidget(self.combomox_y_lattice)
        layout_view_val_2.addWidget(self.combomox_z_lattice)

        layout_range_val.addLayout(layout_view_val_1)
        layout_range_val.addLayout(layout_view_val_2)

        label_B_dir      = QtWidgets.QLabel("B-direction")
        self.combomox_B_dir = QtWidgets.QComboBox()
        self.combomox_B_dir.addItems(["B_x","B_y","B_z"])
        self.combomox_B_dir.setStyleSheet("""
            QComboBox {
                background-color: white;
                color: black;
                border: 1px solid gray;
                padding: 2px;
            }
        """)
        layout_view_val_1.addWidget(label_B_dir   )
        layout_view_val_2.addWidget(self.combomox_B_dir)

        layout_view.addWidget(label_title_view)
        layout_view.addLayout(layout_range_val)
        
        widget_temp_view = QtWidgets.QWidget()        
        widget_temp_view.setLayout(layout_view)
        return widget_temp_view

    def update_xyz_plane_combobox(self):
        self.combomox_x_lattice.clear()
        self.combomox_y_lattice.clear()
        self.combomox_z_lattice.clear()

        x_step = int((internal_parameter.x_view_range_max-internal_parameter.x_view_range_min)/internal_parameter.field_resolution)
        y_step = int((internal_parameter.y_view_range_max-internal_parameter.y_view_range_min)/internal_parameter.field_resolution)
        z_step = int((internal_parameter.z_view_range_max-internal_parameter.z_view_range_min)/internal_parameter.field_resolution)
        x_lattice = np.linspace(internal_parameter.x_view_range_min, internal_parameter.x_view_range_max, x_step+1)
        y_lattice = np.linspace(internal_parameter.y_view_range_min, internal_parameter.y_view_range_max, y_step+1)
        z_lattice = np.linspace(internal_parameter.z_view_range_min, internal_parameter.z_view_range_max, z_step+1)
        
        current_X = internal_parameter.x_view_range_min
        current_Y = internal_parameter.y_view_range_min
        current_Z = internal_parameter.z_view_range_min

        while current_X <= internal_parameter.x_view_range_max:
            self.combomox_x_lattice.addItem(str(current_X))
            current_X += x_step
        while current_Y <= internal_parameter.y_view_range_max:
            self.combomox_y_lattice.addItem(str(current_Y))
            current_Y += y_step
        while current_Z <= internal_parameter.z_view_range_max:
            self.combomox_z_lattice.addItem(str(current_Z))
            current_Z += z_step

        n = self.combomox_x_lattice.count()
        middle_index = n // 2
        self.combomox_x_lattice.setCurrentIndex(middle_index)

        n = self.combomox_y_lattice.count()
        middle_index = n // 2
        self.combomox_y_lattice.setCurrentIndex(middle_index)

        n = self.combomox_z_lattice.count()
        middle_index = n // 2
        self.combomox_z_lattice.setCurrentIndex(middle_index)

        

    def set_dot_line(self,):
        line1 = QtWidgets.QFrame()
        line1.setFixedHeight(1)
        line1.setStyleSheet("border-bottom: 1px dotted black;")
        return line1


    def set_line(self,):
        line1 = QtWidgets.QFrame()
        line1.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        line1.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        return line1

    def run_buttons(self,):
        button_range_save = QtWidgets.QPushButton("Run")
        button_range_save.clicked.connect(lambda: self.func_run())
        button_range_save.setStyleSheet("""
            QPushButton {
                background-color: #aaaaaa;
                color: white;
                font-size: 14px;
                padding: 8px 16px;
                border: none;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #888888;
            }
            QPushButton:pressed {
                background-color: #666666;
            }
        """)
        return button_range_save


    def set_buttons(self,):
        button_range_save = QtWidgets.QPushButton("Set")
        button_range_save.clicked.connect(lambda: self.func_set())
        button_range_save.setStyleSheet("""
            QPushButton {
                background-color: #aaaaaa;
                color: white;
                font-size: 14px;
                padding: 8px 16px;
                border: none;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #888888;
            }
            QPushButton:pressed {
                background-color: #666666;
            }
        """)
        return button_range_save

    def view_buttons(self,):
        button_temp = QtWidgets.QPushButton("View")
        button_temp.clicked.connect(lambda: self.func_view())
        button_temp.setStyleSheet("""
            QPushButton {
                background-color: #aaaaaa;
                color: white;
                font-size: 14px;
                padding: 8px 16px;
                border: none;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #888888;
            }
            QPushButton:pressed {
                background-color: #666666;
            }
        """)
        return button_temp




    def export_buttons(self,):
        button_range_save = QtWidgets.QPushButton("Export")
        button_range_save.clicked.connect(lambda: self.func_export())
        button_range_save.setStyleSheet("""
            QPushButton {
                background-color: #aaaaaa;
                color: white;
                font-size: 14px;
                padding: 8px 16px;
                border: none;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #888888;
            }
            QPushButton:pressed {
                background-color: #666666;
            }
        """)
        return button_range_save


    def set_parameters(self):
        internal_parameter.x_3d_range = float(self.lineedit_3d_xrange.text())
        internal_parameter.y_3d_range = float(self.lineedit_3d_yrange.text())
        internal_parameter.z_3d_range = float(self.lineedit_3d_zrange.text())

        internal_parameter.x_view_range_max    = float(self.lineedit_xmax.text())
        internal_parameter.x_view_range_min    = float(self.lineedit_xmin.text())
        internal_parameter.y_view_range_max    = float(self.lineedit_ymax.text())
        internal_parameter.y_view_range_min    = float(self.lineedit_ymin.text())
        internal_parameter.z_view_range_max    = float(self.lineedit_zmax.text())
        internal_parameter.z_view_range_min    = float(self.lineedit_zmin.text())

        internal_parameter.x_magnet_len = float(self.lineedit_magnet_xlen.text())
        internal_parameter.y_magnet_len = float(self.lineedit_magnet_ylen.text())
        internal_parameter.z_magnet_len = float(self.lineedit_magnet_zlen.text())
        internal_parameter.B_r = float(self.lineedit_br.text())

    def set_view_parameter(self):
        internal_parameter.sliceview_x = float(self.combomox_x_lattice.currentText())
        internal_parameter.sliceview_y = float(self.combomox_y_lattice.currentText())
        internal_parameter.sliceview_z = float(self.combomox_z_lattice.currentText())

        internal_parameter.target_direction =  self.combomox_B_dir.currentText()

    def func_run(self):
        if self.is_set():            
            EventBus.emit(EventBus.ASK_CALCULATION)
        else:
            msg = QtWidgets.QMessageBox()
            msg.setText("Please press 'Set' button before run")
            msg.setWindowTitle("Inform")
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.exec()

        
    def func_set(self):
        self.set_parameters()
        if self.is_min_max_right():
            EventBus.emit(EventBus.SET_BUTTON_CLICKED)
            msg = QtWidgets.QMessageBox()
            msg.setText("Applied")
            msg.setWindowTitle("Inform")
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.exec()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setText("Please check min & max values")
            msg.setWindowTitle("Inform")
            msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            msg.exec()
    
    def func_export(self):
        EventBus.emit(EventBus.EXPORT_BUTTON_CLICKED)
        msg = QtWidgets.QMessageBox()
        msg.setText("Exported")
        msg.setWindowTitle("Inform")
        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msg.exec()


    def is_set(self):
        if internal_parameter.x_3d_range != float(self.lineedit_3d_xrange.text()):
            return False
        if internal_parameter.y_3d_range != float(self.lineedit_3d_yrange.text()):
            return False
        if internal_parameter.z_3d_range != float(self.lineedit_3d_zrange.text()):
            return False

        if internal_parameter.x_view_range_max != float(self.lineedit_xmax.text()):
            return False
        if internal_parameter.x_view_range_min != float(self.lineedit_xmin.text()):
            return False
        if internal_parameter.y_view_range_max != float(self.lineedit_ymax.text()):
            return False
        if internal_parameter.y_view_range_min != float(self.lineedit_ymin.text()):
            return False
        if internal_parameter.z_view_range_max != float(self.lineedit_zmax.text()):
            return False
        if internal_parameter.z_view_range_min != float(self.lineedit_zmin.text()):
            return False

        if internal_parameter.x_magnet_len != float(self.lineedit_magnet_xlen.text()):
            return False
        if internal_parameter.y_magnet_len != float(self.lineedit_magnet_ylen.text()):
            return False
        if internal_parameter.z_magnet_len != float(self.lineedit_magnet_zlen.text()):
            return False
        if internal_parameter.B_r != float(self.lineedit_br.text()):
            return False

        return True

    def is_min_max_right(self):
        if internal_parameter.x_view_range_max < internal_parameter.x_view_range_min:
            return False
        if internal_parameter.y_view_range_max < internal_parameter.y_view_range_min:
            return False
        if internal_parameter.z_view_range_max < internal_parameter.z_view_range_min:
            return False
        return True 

    def func_view(self):
        self.set_view_parameter()
        EventBus.emit(EventBus.SHOW_PLOT)