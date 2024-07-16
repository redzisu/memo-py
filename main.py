import sys
import os
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from mainWindow_ui import Ui_MainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        #==================  Signal  ====================
        self.ui.btn_pathFolder.clicked.connect(self.fn_pathFolder)
        
    #==================  Slot ====================
    def fn_pathFolder(self) :
        user_documents_folder = os.path.expandvars(r'%USERPROFILE%\Documents')  # Default Root: 내 문서
        fname = QFileDialog.getExistingDirectory(self, '폴더 선택', user_documents_folder, QFileDialog.ShowDirsOnly)
        #self.ui.ibx_downPath.setText(fname)
    
    # Alert창 
    def fn_alertBox(self, pStr): 
        msgBox = QMessageBox()
        msgBox.setText(pStr)
        msgBox.exec() 
    
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    window = MainWindow()        
    window.show()                 
    sys.exit(app.exec())         
   