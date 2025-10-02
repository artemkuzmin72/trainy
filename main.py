import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.opac = 1
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Example')
        self.setGeometry(300, 300, 300, 300)
        
        self.original_width = 300
        self.original_height = 300

        self.button1 = QPushButton("-", self)
        self.button1.move(200, 0)
        self.button1.setGeometry(200, 0, 40, 30)
        self.button1.clicked.connect(self.opacity_minus)

        self.button2 = QPushButton("+", self)
        self.button2.move(250, 0)
        self.button2.setGeometry(200, 0, 40, 30)
        self.button2.clicked.connect(self.opacity_plus)

    def opacity_minus(self):
        if self.opac > 0.5:  
            self.opac -= 0.1
            self.setWindowOpacity(self.opac)

    def opacity_plus(self):
        if self.opac < 1.0:
            self.opac += 0.1
            self.setWindowOpacity(self.opac)

    def resizeEvent(self, event):
        """Вызывается автоматически при изменении размера окна"""
        super().resizeEvent(event)

        width = self.size().width()    
        height = self.size().height()   

        koefW = width / self.original_width 
        koefH = height / self.original_height 

        self.button1.setGeometry(
            int(200 * koefW), int(0 * koefH), 
            40, 30  
        )
        self.button2.setGeometry(
            int(250 * koefW), int(0 * koefH), 
            40, 30  
        )

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Example()
    w.show()
    sys.exit(app.exec_())