# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.6.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_remote(object):
    def setupUi(self, remote):
        remote.setObjectName("remote")
        remote.resize(273, 652)
        self.gridLayoutWidget = QtWidgets.QWidget(parent=remote)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 251, 421))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.volume_down_button = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.volume_down_button.setMinimumSize(QtCore.QSize(0, 150))
        self.volume_down_button.setMaximumSize(QtCore.QSize(95, 16777215))
        self.volume_down_button.setObjectName("volume_down_button")
        self.gridLayout.addWidget(self.volume_down_button, 3, 0, 1, 1)
        self.volume_up_button = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.volume_up_button.setMinimumSize(QtCore.QSize(0, 150))
        self.volume_up_button.setMaximumSize(QtCore.QSize(95, 16777215))
        self.volume_up_button.setObjectName("volume_up_button")
        self.gridLayout.addWidget(self.volume_up_button, 2, 0, 1, 1)
        self.channe_up_button = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.channe_up_button.setMinimumSize(QtCore.QSize(0, 150))
        self.channe_up_button.setMaximumSize(QtCore.QSize(95, 16777215))
        self.channe_up_button.setObjectName("channe_up_button")
        self.gridLayout.addWidget(self.channe_up_button, 2, 1, 1, 1)
        self.channe_down_button = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.channe_down_button.setMinimumSize(QtCore.QSize(0, 150))
        self.channe_down_button.setMaximumSize(QtCore.QSize(95, 16777215))
        self.channe_down_button.setObjectName("channe_down_button")
        self.gridLayout.addWidget(self.channe_down_button, 3, 1, 1, 1)
        self.mute_button = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.mute_button.setMinimumSize(QtCore.QSize(0, 75))
        self.mute_button.setObjectName("mute_button")
        self.gridLayout.addWidget(self.mute_button, 0, 1, 1, 1)
        self.power_button = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.power_button.setMinimumSize(QtCore.QSize(0, 75))
        self.power_button.setAcceptDrops(False)
        self.power_button.setObjectName("power_button")
        self.gridLayout.addWidget(self.power_button, 0, 0, 1, 1)
        self.tv_status = QtWidgets.QTextEdit(parent=remote)
        self.tv_status.setGeometry(QtCore.QRect(10, 460, 251, 181))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tv_status.setFont(font)
        self.tv_status.setReadOnly(True)
        self.tv_status.setObjectName("tv_status")

        self.retranslateUi(remote)
        QtCore.QMetaObject.connectSlotsByName(remote)

    def retranslateUi(self, remote):
        _translate = QtCore.QCoreApplication.translate
        remote.setWindowTitle(_translate("remote", "Remote"))
        self.volume_down_button.setText(_translate("remote", "Volume Down"))
        self.volume_up_button.setText(_translate("remote", "Volume Up"))
        self.channe_up_button.setText(_translate("remote", "Channel Up"))
        self.channe_down_button.setText(_translate("remote", "Channel Down"))
        self.mute_button.setText(_translate("remote", "Mute"))
        self.power_button.setText(_translate("remote", "Power"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    remote = QtWidgets.QDialog()
    ui = Ui_remote()
    ui.setupUi(remote)
    remote.show()
    sys.exit(app.exec())
