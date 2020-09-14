from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.init_UI()

    def init_UI(self):
        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle('Trisate CheckBox')

        checkbox1 = QCheckBox('Small', self)
        checkbox2 = QCheckBox('Medium', self)
        checkbox3 = QCheckBox('Large', self)
        group = QButtonGroup(self)

        group.addButton(checkbox1)
        group.addButton(checkbox2)
        group.addButton(checkbox3)

        self.lbl = QLabel('.', self)

        hbox = QHBoxLayout()
        hbox.addWidget(checkbox1)
        hbox.addWidget(checkbox2)
        hbox.addWidget(checkbox3)
        vbox = QVBoxLayout()

        vbox.addLayout(hbox)
        vbox.addSpacing(20)
        vbox.addWidget(self.lbl)
        self.setLayout(vbox)
        group.buttonClicked.connect(self.label_text_show)

    def label_text_show(self, btn):

        self.lbl.setText(btn.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Example()
    win.show()

    sys.exit(app.exec_())
