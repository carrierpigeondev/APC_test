from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel

class GUI:
    def __init__(self):
        app = QApplication([])

        window = QMainWindow()

        widget = QWidget()

        layout = QGridLayout()
        widget.setLayout(layout)

        window.setCentralWidget(widget)
        window.setWindowTitle("PyQt App")
        
        ### Your GUI code goes below this line ###
        
        
        
        ### Your GUI code goes above this line ###

        window.show()
        app.exec_()
        
if __name__ == "__main__":
    gui = GUI()
