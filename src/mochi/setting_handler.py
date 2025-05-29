from PyQt6 import QtWidgets
from PyQt6.QtCore import Qt

class setting_handler:
    def __init__(self,):
        return
    
    def widget_settings(self,):
        layout_settings = QtWidgets.QHBoxLayout()
        layout_settings_labels = QtWidgets.QVBoxLayout()
        layout_settings_lineedit = QtWidgets.QVBoxLayout()



        layout_settings.addLayout(layout_settings_labels)
        layout_settings.addLayout(layout_settings_lineedit)
        # layout_settings
        
        save_buttons = self.save_buttons()
        cancel_buttons = self.cancel_buttons()
        layout_settings.addWidget(save_buttons)
        layout_settings.addWidget(cancel_buttons)


        return layout_settings



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


    def cancel_buttons(self,):
        button_range_cancel = QtWidgets.QPushButton("Cancel")
        button_range_cancel.clicked.connect(lambda: self.func_cancel())
        button_range_cancel.setStyleSheet("""
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
        return button_range_cancel




    def func_set(self):
        msg = QtWidgets.QMessageBox()
        msg.setText("Applied (Not really)")
        msg.setWindowTitle("Inform")
        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msg.exec()

    
    def func_cancel(self):
        msg = QtWidgets.QMessageBox()
        msg.setText("Cancsled")
        msg.setWindowTitle("Inform")
        msg.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        msg.exec()



