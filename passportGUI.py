# import sys and os
import sys
import os

# import QT5
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QHBoxLayout, QVBoxLayout, QGroupBox, QDialog
from PyQt5.QtWidgets import QPushButton, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot

# this is a test, it produces an image for us from the pillow library
from PIL import Image

# this is to import the ocr-doc_read script, allows us to use the methods in it
from ocrdoc_read import detect_document, to_file, set_key

# this is to import the nofly comparison script, allows us to use the methods in it
from nofly_comparison import *

class App(QDialog):
    def __init__(self):
        super().__init__()
        self.title = 'Passport Checker'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createGridLayout()

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
        self.show()

    def createGridLayout(self):
        # instantiation of the grid layout and its components
        self.horizontalGroupBox = QGroupBox("")
        layout = QGridLayout()
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 4)

        # set a set of text to be overwritten with "Match" or "No Matches", lower left
        inputResults = "This is the beginning of\nthe MRZ screen. Please\nscan a photo."
        results = QLabel(inputResults)

        # button to call the comparison with the selected file, lower right
        scan = QPushButton("Scan")
        scan.clicked.connect(self.readAndCompare)

        # selecting a file, most likely a button, function used?, placed in lower middle
        selectFile = QPushButton("Select File")
        selectFile.clicked.connect(self.fileSelection)

        # resulting amount of matches, text to be overwritten, upper right
        totalMatches = "This is where the total amount of matches\nwill be displayed when scanned."
        matches = QLabel(totalMatches)

        # this places the above creations into a grid to be displayed
        layout.addWidget(results,1,0)
        layout.addWidget(selectFile,1,1)
        layout.addWidget(matches,0,2)
        layout.addWidget(scan,1,2)

        self.horizontalGroupBox.setLayout(layout)

    # this provides us with a full string of the selected image's location.
    @pyqtSlot()
    def fileSelection(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            name = fileName
            image = Image.open(fileName)
            image.show()
            print(name)
            set_key('Software_Engineering_Team7_OCR-c578ecae6914.json')
            wordArray = detect_document(name)
            to_file(wordArray,0)

    # this provides functionality to the scan button, activates comparison algorithm
    @pyqtSlot()
    def readAndCompare(self):
        confidence_flip_flop()
        matches = comparison_Alg()
        if matches >= 1:
            QMessageBox.warning(self, "Results", "Multiple  close matches found! Check the passport before "
                                                 "alerting security.")
        else:
            QMessageBox.information(self, "Results", "No close matches found!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())