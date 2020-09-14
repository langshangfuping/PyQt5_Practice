import sys

from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QDialog

import Qt_Ui
# rgr
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QDialog()
    ui = Qt_Ui.Ui_Dialog()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
