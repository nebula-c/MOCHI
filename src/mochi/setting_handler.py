from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt

class setting_handler:
    def __init__(self,):
        self.xmin   =   -100
        self.xmax   =    100
        self.ymin   =   -100
        self.ymax   =    100
        self.zmin   =   -100
        self.zmax   =    100
    
    def SetParameters(self,parameter_input):
        self.internal_parameter = parameter_input

    def widget_settings(self,):
        layout_settings = QtWidgets.QVBoxLayout()
        layout_buttons = QtWidgets.QHBoxLayout()
        
        widget_3d_range = self.widget_3d_range()
        widget_3d_range.setContentsMargins(0, 0, 0, 0)
        layout_settings.addWidget(widget_3d_range)


        line1 = self.set_line()
        layout_settings.addWidget(line1)
        layout_settings.addStretch()

        widget_view_range = self.widget_view_range()
        widget_view_range.setContentsMargins(0, 0, 0, 0)
        layout_settings.addWidget(widget_view_range)

        line2 = self.set_line()
        layout_settings.addWidget(line2)
        layout_settings.addStretch()

        widget_magnet_val = self.widget_magnet_val()
        widget_magnet_val.setContentsMargins(0, 0, 0, 0)
        layout_settings.addWidget(widget_magnet_val)


        line3 = self.set_line()
        layout_settings.addWidget(line3)
        layout_settings.addStretch()



        widget_view = self.widget_view()
        widget_view.setContentsMargins(0, 0, 0, 0)
        layout_settings.addWidget(widget_view)

        line4 = self.set_line()
        layout_settings.addWidget(line4)
        layout_settings.addStretch()



        set_buttons = self.set_buttons()
        export_buttons = self.export_buttons()
        layout_buttons.addWidget(set_buttons)
        layout_buttons.addWidget(export_buttons)
        layout_settings.addLayout(layout_buttons)


        widget_temp_setting = QtWidgets.QWidget()        
        widget_temp_setting.setLayout(layout_settings)
        return widget_temp_setting


    def widget_3d_range(self,):
        label_title_range      = QtWidgets.QLabel("3D range")
        
        layout_range = QtWidgets.QVBoxLayout()
        layout_range_val = QtWidgets.QVBoxLayout()
        layout_x_range = QtWidgets.QHBoxLayout()
        layout_y_range = QtWidgets.QHBoxLayout()
        layout_z_range = QtWidgets.QHBoxLayout()
        

        label_xmax      = QtWidgets.QLabel("X range")
        lineedit_xmax   = QtWidgets.QLineEdit("{}".format(self.internal_parameter.x_3d_range))
        layout_x_range.addWidget(label_xmax   )
        layout_x_range.addWidget(lineedit_xmax)

        label_ymax      = QtWidgets.QLabel("Y range")
        lineedit_ymax   = QtWidgets.QLineEdit("{}".format(self.internal_parameter.y_3d_range))
        layout_y_range.addWidget(label_ymax   )
        layout_y_range.addWidget(lineedit_ymax)

        label_zmax      = QtWidgets.QLabel("Z range")
        lineedit_zmax   = QtWidgets.QLineEdit("{}".format(self.internal_parameter.z_3d_range))
        layout_z_range.addWidget(label_zmax   )
        layout_z_range.addWidget(lineedit_zmax)
        

        layout_range.addWidget(label_title_range,stretch=1)
        layout_range_val.addLayout(layout_x_range,stretch=1)
        layout_range_val.addLayout(layout_y_range,stretch=1)
        layout_range_val.addLayout(layout_z_range,stretch=1)
        layout_range.addLayout(layout_range_val)

        widget_temp_range = QtWidgets.QWidget()        
        widget_temp_range.setLayout(layout_range)
        return widget_temp_range


    def widget_view_range(self,):
        label_title_range      = QtWidgets.QLabel("View range")
        
        layout_range = QtWidgets.QVBoxLayout()
        layout_range_val = QtWidgets.QVBoxLayout()
        layout_x_range = QtWidgets.QHBoxLayout()
        layout_y_range = QtWidgets.QHBoxLayout()
        layout_z_range = QtWidgets.QHBoxLayout()
        
        label_xmin      = QtWidgets.QLabel("xmin")
        lineedit_xmin   = QtWidgets.QLineEdit("{}".format(self.internal_parameter.x_view_range_min))
        label_xmax      = QtWidgets.QLabel("xmax")
        lineedit_xmax   = QtWidgets.QLineEdit("{}".format(self.internal_parameter.x_view_range_max))
        layout_x_range.addWidget(label_xmin   )
        layout_x_range.addWidget(lineedit_xmin)
        layout_x_range.addWidget(label_xmax   )
        layout_x_range.addWidget(lineedit_xmax)

        label_ymin      = QtWidgets.QLabel("ymin")
        lineedit_ymin   = QtWidgets.QLineEdit("{}".format(self.internal_parameter.y_view_range_min))
        label_ymax      = QtWidgets.QLabel("ymax")
        lineedit_ymax   = QtWidgets.QLineEdit("{}".format(self.internal_parameter.y_view_range_max))
        layout_y_range.addWidget(label_ymin   )
        layout_y_range.addWidget(lineedit_ymin)
        layout_y_range.addWidget(label_ymax   )
        layout_y_range.addWidget(lineedit_ymax)

        label_zmin      = QtWidgets.QLabel("zmin")
        lineedit_zmin   = QtWidgets.QLineEdit("{}".format(self.internal_parameter.z_view_range_min))
        label_zmax      = QtWidgets.QLabel("zmax")
        lineedit_zmax   = QtWidgets.QLineEdit("{}".format(self.internal_parameter.z_view_range_max))
        layout_z_range.addWidget(label_zmin   )
        layout_z_range.addWidget(lineedit_zmin)
        layout_z_range.addWidget(label_zmax   )
        layout_z_range.addWidget(lineedit_zmax)
        
        layout_range.addWidget(label_title_range,stretch=1)
        layout_range_val.addLayout(layout_x_range,stretch=1)
        layout_range_val.addLayout(layout_y_range,stretch=1)
        layout_range_val.addLayout(layout_z_range,stretch=1)
        layout_range.addLayout(layout_range_val)

        widget_temp_range = QtWidgets.QWidget()        
        widget_temp_range.setLayout(layout_range)
        return widget_temp_range


    def widget_magnet_val(self,):
        label_title_range      = QtWidgets.QLabel("Magnet setting")
        
        layout_magnet = QtWidgets.QVBoxLayout()
        layout_magnet_val_1 = QtWidgets.QHBoxLayout()
        layout_magnet_val_2 = QtWidgets.QHBoxLayout()
        layout_x_range = QtWidgets.QHBoxLayout()
        layout_y_range = QtWidgets.QHBoxLayout()
        layout_z_range = QtWidgets.QHBoxLayout()
        layout_br = QtWidgets.QHBoxLayout()
        
        label_xlen      = QtWidgets.QLabel("x length")
        lineedit_xlen   = QtWidgets.QLineEdit("{}".format(self.internal_parameter.x_magnet_len))
        layout_x_range.addWidget(label_xlen   )
        layout_x_range.addWidget(lineedit_xlen)

        label_ylen      = QtWidgets.QLabel("y length")
        lineedit_ylen   = QtWidgets.QLineEdit("{}".format(self.internal_parameter.y_magnet_len))
        layout_y_range.addWidget(label_ylen   )
        layout_y_range.addWidget(lineedit_ylen)

        label_zlen      = QtWidgets.QLabel("z length")
        lineedit_zlen   = QtWidgets.QLineEdit("{}".format(self.internal_parameter.z_magnet_len))
        layout_z_range.addWidget(label_zlen   )
        layout_z_range.addWidget(lineedit_zlen)

        label_br      = QtWidgets.QLabel("B_r")
        lineedit_br   = QtWidgets.QLineEdit("{}".format(self.internal_parameter.B_r))
        layout_br.addWidget(label_br   )
        layout_br.addWidget(lineedit_br)
        
        layout_magnet.addWidget(label_title_range)
        layout_magnet_val_1.addLayout(layout_x_range,stretch=1)
        layout_magnet_val_1.addLayout(layout_y_range,stretch=1)
        layout_magnet_val_2.addLayout(layout_z_range,stretch=1)
        layout_magnet_val_2.addLayout(layout_br,stretch=1)
        layout_magnet.addLayout(layout_magnet_val_1)
        layout_magnet.addLayout(layout_magnet_val_2)
        
        widget_temp_magnet = QtWidgets.QWidget()        
        widget_temp_magnet.setLayout(layout_magnet)
        return widget_temp_magnet


    def widget_view(self,):
        label_title_view      = QtWidgets.QLabel("View setting")
        
        layout_view = QtWidgets.QVBoxLayout()
        layout_view_val_1 = QtWidgets.QHBoxLayout()
        
        label_plane_choose      = QtWidgets.QLabel("Choose plane")
        combo_plane_axis = QtWidgets.QComboBox()
        combo_plane_axis.addItems(["X","Y","Z"])
        combo_plane_axis.setCurrentIndex(2) ## Default as "Z"
        combo_plane_axis.setStyleSheet("""
            QComboBox {
                min-width: 30px;
                color: black;
                border: 1px solid gray;
                padding: 5px;
            }
        """)
        combo_plane_axis.currentTextChanged.connect(lambda text: setattr(self,'plane_axis', text))
        plane_axis =  combo_plane_axis.itemText(0)

        label_equal = QtWidgets.QLabel(" = ")
        lineedit_axis_val   = QtWidgets.QLineEdit("0")

        layout_view_val_1.addWidget(label_plane_choose)
        layout_view_val_1.addWidget(combo_plane_axis)
        layout_view_val_1.addWidget(label_equal)
        layout_view_val_1.addWidget(lineedit_axis_val)
        
        layout_view.addWidget(label_title_view)
        layout_view.addLayout(layout_view_val_1)
        
        widget_temp_view = QtWidgets.QWidget()        
        widget_temp_view.setLayout(layout_view)
        return widget_temp_view

    def set_line(self,):
        line1 = QtWidgets.QFrame()
        line1.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        line1.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        return line1


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





    # def func_set(self):
    #     msg = QtWidgets.QMessageBox()
    #     msg.setText("Applied (Not really)")
    #     msg.setWindowTitle("Inform")
    #     msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
    #     msg.exec()

    
    # def func_export(self):
    #     msg = QtWidgets.QMessageBox()
    #     msg.setText("Exported (Not really)")
    #     msg.setWindowTitle("Inform")
    #     msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
    #     msg.exec()


