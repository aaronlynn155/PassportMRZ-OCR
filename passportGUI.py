#import sys
import sys

#import QT
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QHBoxLayout, QVBoxLayout, QGroupBox, QDialog
from PyQt5.QtWidgets import QPushButton, QFileDialog, QImage
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot

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
        self.horizontalGroupBox = QGroupBox("Grid")
        layout = QGridLayout()
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 4)

		resultingDoc = None

        # set an image to the label, upper left. currently not working, commented out for testing purposes
	'''
        picture = QLabel()
        pixmap = QPixmap("testPic")
        pixmap = pixmap.scaledToWidth(200)
        picture.setPixmap(pixmap)
	'''

        # set a set of text to be overwritten with "Match" or "No Matches", lower left
        inputResults = "This is the beginning of\nthe MRZ screen. Please\nscan a photo."
        results = QLabel(inputResults)

        # button to call the comparison with the selected file, lower right
        scan = QPushButton("Scan")

        # selecting a file, most likely a button, function used?, placed in lower middle
        selectFile = QPushButton("Select File")
        selectFile.clicked.connect(self.fileSelection)

        # resulting amount of matches, text to be overwritten, upper right
        totalMatches = "This is where the total amount of matches\nwill be displayed when scanned."
        matches = QLabel(totalMatches)

        # this places the above creations into a grid to be displayed
        #layout.addWidget(picture,0,0)									Commented out for testing puproses. Displays picture.
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
            print(fileName)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())