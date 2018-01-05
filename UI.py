import sys
from PyQt5.QtCore import QSize, QBasicTimer, Qt
from PyQt5.QtGui import QImage, QPalette, QBrush, QFont
from PyQt5.QtWidgets import *

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setGeometry(100, 100, 900, 395)

        oImage = QImage("minion_background.gif")
        # resize Image to widgets size
        sImage = oImage.scaled(QSize(900, 395))
        palette = QPalette()
        # 10 = Windowrole
        palette.setBrush(10, QBrush(sImage))
        self.setPalette(palette)
        self.timer = QBasicTimer()
        self.step = 0

        # test, if it's really backgroundimage
        # self.label = QLabel('Test', self)
        # self.label.setGeometry(50, 50, 200, 50)

        self.pbar = []
        parts = ['Upper Arm', 'Lower Arm', 'Leg']
        for i, part in enumerate(parts):
            part_name = 'Left ' + part
            label = QLabel(part_name, self)
            f = QFont("Arial", 14)
            label.setGeometry(50, 40+ i * 120, 200, 30)
            label.setFont(f)
            bar = QProgressBar(self)
            bar.setGeometry(50, 70 + i * 120, 200, 30)
            self.pbar.append(bar)
        for i in range(3):
            part_name = 'Right ' + part
            label = QLabel(part_name, self)
            f = QFont("Arial", 14)
            label.setGeometry(650, 40+ i * 120, 200, 30)
            label.setFont(f)

            bar = QProgressBar(self)
            bar.setGeometry(650, 70 + i * 120, 200, 30)
            self.pbar.append(bar)

        self.show()
        self.timer.start(100, self)

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.setWindowState(self.windowState() & ~Qt.WindowMinimized | Qt.WindowActive)
            # this will activate the window
            self.activateWindow()
            return
        self.step = self.step + 5
        [bar.setValue(self.step) for bar in self.pbar]

    

if __name__ == "__main__":

    app = QApplication(sys.argv)
    oMainwindow = MainWindow()
    sys.exit(app.exec_())
