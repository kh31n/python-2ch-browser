# main.py 2ch Browser with Python3
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import glob
import os

def file_browser(path,parentItem):
    for file in sorted(glob.glob(path + "/*")):
        item = QStandardItem(os.path.basename(file))
        parentItem.appendRow(item)
        if os.path.isdir(file):
            file_browser(file, item)

def on_button_clicked():
    alert = QMessageBox()
    alert.setText('You clicked the button!')
    alert.exec_()

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
button = QPushButton('Click')
treeview = QTreeView()
home = os.path.expanduser("~")
path = home + "/Dropbox/rails/rblog"
model = QStandardItemModel(0,1)
model.setHeaderData(0,Qt.Horizontal,"File")
parentItem = model.invisibleRootItem()
file_browser(path,parentItem)
button.clicked.connect(on_button_clicked)
treeview.setModel(model)
layout.addWidget(treeview)
layout.addWidget(button)
window.setLayout(layout)
window.show()
app.exec_()
