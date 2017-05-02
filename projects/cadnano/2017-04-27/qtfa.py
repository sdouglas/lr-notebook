# http://stackoverflow.com/questions/35129052/load-fontawesome-in-pyqt-app

from PyQt5.QtGui import QFontDatabase
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolButton


class MainWindow(QMainWindow):
    css = """
        QToolButton{{
            border: None;
        }}
    """

    def __init__(self):
        super(MainWindow, self).__init__()

        font_id = QFontDatabase.addApplicationFont("fontawesome-webfont.ttf")

        if font_id is not -1:
            font_db = QFontDatabase()
            self.font_styles = font_db.styles('FontAwesome')
            self.font_families = QFontDatabase.applicationFontFamilies(font_id)
            print(self.font_styles, self.font_families)
            for font_family in self.font_families:
                self.font = font_db.font(font_family, self.font_styles[0], 18)
        self.home()

    def home(self):
        self.setStyleSheet(self.css.format())

        btn = QToolButton(self)
        btn.setToolButtonStyle(Qt.ToolButtonIconOnly)
        btn.setFont(self.font)
        btn.setText(chr(int('f023', 16)) + " " + chr(int('f06e', 16)))         # 'f023' lock 'f06e' eye
        btn.clicked.connect(QCoreApplication.instance().quit)
        self.show()

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

sys.exit(app.exec_())
