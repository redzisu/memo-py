import sys
import os
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from mainWindow_ui import Ui_MainWindow
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        #==================  Default Setting  ====================
        # QListWidget
        # self.ui.grd_list.setMinimumWidth(self.ui.grd_list.sizeHintForColumn(0))
        
        #==================  Signal  ====================
        self.ui.btn_insertRow.clicked.connect(self.fn_insertRow)
        self.ui.btn_deleteRow.clicked.connect(lambda : self.fn_confirm(
            "삭제하시겠습니까?", 
            lambda: self.fn_deleteRow(), 
            lambda: None
            )) 
        
        self.ui.grd_list.itemActivated.connect(self.fn_editRow)
        
    #==================  Slot ====================
    # 리스트 행 추가
    def fn_insertRow(self) :
        item = QListWidgetItem('')
        # item.setBackground(QColor('yellow'))  # 배경색을 초록색으로 설정합니다.
        self.ui.grd_list.addItem(item)
        self.ui.grd_list.openPersistentEditor(item)
        self.ui.grd_list.setCurrentItem(item)
        
    # 리스트 행 편집
    def fn_editRow(self) :
        item = self.ui.grd_list.currentItem()
        if (self.ui.grd_list.isPersistentEditorOpen(item)) :
            self.ui.grd_list.closePersistentEditor(item)
        else :
            self.ui.grd_list.openPersistentEditor(item)
    
    # 리스트 행 삭제
    def fn_deleteRow(self) :
        row = self.ui.grd_list.currentRow()
        self.ui.grd_list.takeItem(row)
            
    
    # 폴더 선택창 열기 (기본경로는 '내 문서'로 설정)
    def fn_openFolder(self) :
        user_documents_folder = os.path.expandvars(r'%USERPROFILE%\Documents')  
        fname = QFileDialog.getExistingDirectory(self, '폴더 선택', user_documents_folder, QFileDialog.ShowDirsOnly)
        #self.ui.ibx_downPath.setText(fname)
        
    # Alert창 
    # @param 메시지
    def fn_alert(self, pStr): 
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Alert")
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setText(pStr)
        msgBox.exec() 
        
    # Confirm창 
    # @param 메시지
    def fn_confirm(self, pStr, pCallback_yes, pCallback_no): 
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Confirm")
        msgBox.setIcon(QMessageBox.Question)
        msgBox.setText(pStr)
        msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Cancel)
        msgBox.button(QMessageBox.Save).setText("확인")
        msgBox.button(QMessageBox.Cancel).setText("취소")
        ret = msgBox.exec() 
        
        if ret == QMessageBox.Save:
            pCallback_yes()
        else:
            pCallback_no()
    
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    window = MainWindow()        
    window.show()                 
    sys.exit(app.exec())         
   