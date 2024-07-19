import sys
import os
import clipboard
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from pyqttoast import Toast, ToastPreset, ToastPosition

from mainWindow_ui import Ui_MainWindow

class TextEditDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        editor = QTextEdit(parent)
        editor.setLineWrapMode(QTextEdit.WidgetWidth) 
        editor.setFixedHeight(editor.fontMetrics().lineSpacing() * 3)  # 3줄 높이로 설정
        return editor

    def setEditorData(self, editor, index):
        text = index.model().data(index, Qt.EditRole)
        editor.setPlainText(text)

    def setModelData(self, editor, model, index):
        text = editor.toPlainText()
        model.setData(index, text, Qt.EditRole)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)
        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        #==================  Default Setting  ====================
        # QListWidget
        # self.ui.grd_list.setMinimumWidth(self.ui.grd_list.sizeHintForColumn(0))
        
        # QListWidget 텍스트 편집 커스텀
        self.ui.grd_list.setItemDelegate(TextEditDelegate())
        
        #==================  Signal  ====================
        self.ui.btn_editRow.clicked.connect(self.fn_editRow)
        self.ui.btn_insertRow.clicked.connect(self.fn_insertRow)
        self.ui.btn_deleteRow.clicked.connect(lambda : self.fn_confirm(
            "삭제하시겠습니까?", 
            lambda: self.fn_deleteRow(), 
            lambda: None
            )) 
        
        self.ui.grd_list.itemClicked.connect(self.fn_copyRow)
        self.ui.grd_list.keyPressEvent = self.event_keyPress
        
    #==================  Slot ====================
    # 리스트 행 추가
    def fn_insertRow(self) :
        item = QListWidgetItem('')
        self.ui.grd_list.addItem(item)
        self.ui.grd_list.setCurrentItem(item)
        self.ui.grd_list.openPersistentEditor(item)
        
    # 리스트 행 편집
    def fn_editRow(self) :
        item = self.ui.grd_list.currentItem()
        if (self.ui.grd_list.isPersistentEditorOpen(item) == False) :
            self.ui.grd_list.openPersistentEditor(item)
    
    # 리스트 keyPress 이벤트
    def event_keyPress(self, event):
        if event.key() == Qt.Key_Return :
            self.fn_editEndRow()
            
            
    # 리스트 행 편집종료
    def fn_editEndRow(self) :
        items = [self.ui.grd_list.item(x) for x in range(self.ui.grd_list.count())]
        
        for item in items :
            if (self.ui.grd_list.isPersistentEditorOpen(item)) :
                self.ui.grd_list.closePersistentEditor(item)
            if (item.text().strip() == '') :
                self.ui.grd_list.takeItem(self.ui.grd_list.row(item))

    # 리스트 행 삭제
    def fn_deleteRow(self) :
        row = self.ui.grd_list.currentRow()
        self.ui.grd_list.takeItem(row)
        
    # 리스트 행 복사
    def fn_copyRow(self) :
        copyText = self.ui.grd_list.currentItem().text()
        clipboard.copy(copyText)
        self.fn_toast("복사 성공")
            
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
    
    # Toast창
    # https://github.com/niklashenning/pyqttoast?tab=readme-ov-file
    def fn_toast(self, pStr):
        toast = Toast(self)
        toast.setDuration(1000)  # 1초
        toast.setTitle(pStr)
        Toast.setMaximumOnScreen(3) # 화면에 maximum 1개
        toast.applyPreset(ToastPreset.SUCCESS)
        toast.setIconSize(QSize(14, 14))
        toast.setShowCloseButton(False)
        toast.setFadeInDuration(100)  
        toast.setFadeOutDuration(150)
        toast.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    window = MainWindow()        
    window.show()                 
    sys.exit(app.exec())         
   