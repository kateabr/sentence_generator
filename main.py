from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class MainWindow(QWidget):
    def __init__(self, parent = None):
        super().__init__()

        self._button: QPushButton = QPushButton("Click")

        self._layout: QVBoxLayout = QVBoxLayout()
        self._layout.addWidget(self._button)

        self.setLayout(self._layout)

        self._button.clicked.connect(lambda x : print(x))




if __name__ == "__main__":
    import sys
    app: QApplication = QApplication(sys.argv)

    window: MainWindow = MainWindow()
    window.show()

    sys.exit(app.exec_())
