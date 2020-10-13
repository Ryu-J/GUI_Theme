################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
## This project can be used freely for all uses, as long as they maintain the
## respective credits only in the Python scripts, any information in the visual
## interface (GUI) can be modified without any implication.
##
## There are limitations on Qt licenses if you want to use your products
## commercially, I recommend reading them on the official website:
## https://doc.qt.io/qtforpython/licenses.html
##
################################################################################

## ==> GUI FILE
from main import *
from ui_main import *
# from video import *
import sqlite3

class Functions(MainWindow):
    pass

    ##웹캠 컨트롤
    # def onoffCam(self, e):
    #         if self.pushButton_2.isChecked():
    #             self.pushButton_2.setText('stop cam')
    #             self.video.startCam()
    #         else:
    #             self.pushButton_2.setText('start cam')
    #             self.video.stopCam()

    # def recvImage(self, img):
    #         self.frm.setPixmap(QPixmap.fromImage(img))

    # def closeEvent(self, e):
    #         self.video.stopCam()

