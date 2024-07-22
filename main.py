import sys
import os
import clipboard
import pickle
import customStyle
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from pyqttoast import Toast, ToastPreset, ToastPosition
from mainWindow_ui import Ui_MainWindow

# QListWidget 커스텀 텍스트 편집
# LineEdit -> TextEdit : multiline 입력 및 수정 가능하도록 수정
class TextEditDelegate(QStyledItemDelegate):
    def __init__(self, list_widget, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.list_widget = list_widget
        
    def createEditor(self, parent, option, index):
        editor = QTextEdit(parent)
        return editor
    
    def setEditorData(self, editor, index):
        if self.list_widget.count() > 0 :
            text = index.model().data(index, Qt.EditRole)
            editor.setPlainText(text)
   
    def setModelData(self, editor, model, index):
        text = editor.toPlainText()
        model.setData(index, text, Qt.EditRole)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)

    def sizeHint(self, option, index):
        height = self.list_widget.viewport().height() / 3
        return QSize(option.rect.width(), height)
    
    def paint(self, painter, option, index):
        option.displayAlignment = Qt.AlignTop | Qt.AlignLeft
        super().paint(painter, option, index)
        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.setWindowTitle("Work-Assist")
        self.setWindowIcon(QIcon.fromTheme("emblem-favorite"))  # 아이콘 ☆
        
        #==================  Default Setting  ====================
        # QListWidget 커스텀 텍스트 편집 
        self.ui.grd_list.setItemDelegate(TextEditDelegate(self.ui.grd_list))
        
        # QListWidget 데이터 불러오기
        with open("data.pickle", "rb") as f: # rb : 바이트 형식으로 읽어오기
            data = pickle.load(f) 
        self.ui.grd_list.insertItems(0, data)
        
        # 버튼 css 설정
        self.ui.btn_editList.setProperty("class", "custom btn-blue") 
        self.ui.btn_insertList.setProperty("class", "custom btn-grey") 
        self.ui.btn_deleteList.setProperty("class", "custom btn-red") 
        
        #==================  Signal  ====================
        self.ui.btn_insertList.clicked.connect(self.fn_insertList)
        self.ui.btn_deleteList.clicked.connect(lambda : self.fn_confirm(
            "삭제하시겠습니까?", 
            lambda: self.fn_deleteList(), 
            lambda: None
            )) 
        self.ui.btn_editList.clicked.connect(self.fn_editList)
        
        self.ui.grd_list.itemClicked.connect(self.fn_copyList)
        self.ui.grd_list.keyPressEvent = self.event_keyPress
        
    #==================  Slot ====================
    # 리스트 행 추가
    def fn_insertList(self) :
        self.fn_editEndList()
         
        item = QListWidgetItem('')
        self.ui.grd_list.addItem(item)
        self.ui.grd_list.setCurrentItem(item)
        self.ui.grd_list.openPersistentEditor(item)
        
    # 리스트 행 편집
    def fn_editList(self) :
        item = self.ui.grd_list.currentItem()
        if (self.ui.grd_list.isPersistentEditorOpen(item) == False) :
            self.ui.grd_list.openPersistentEditor(item)
    
    # 리스트 저장
    def fn_saveList(self) :
        itemData = [self.ui.grd_list.item(x).text() for x in range(self.ui.grd_list.count())]
        
        with open("data.pickle", "wb") as f: # wb : 바이트 형식으로 쓰기
            pickle.dump(itemData, f) 
            
    # 리스트 keyPress 이벤트
    def event_keyPress(self, event):
        if event.key() == Qt.Key_Return and event.modifiers() & Qt.ControlModifier:
            self.fn_editEndList()
            
    # 리스트 행 편집종료
    def fn_editEndList(self) :
        items = [self.ui.grd_list.item(x) for x in range(self.ui.grd_list.count())]
        
        for item in reversed(items):
            if (self.ui.grd_list.isPersistentEditorOpen(item)) :
                self.ui.grd_list.closePersistentEditor(item)
            if not item.text().strip():
                self.ui.grd_list.takeItem(self.ui.grd_list.row(item))
        self.fn_saveList()
        
    # 리스트 행 삭제
    def fn_deleteList(self) :
        row = self.ui.grd_list.currentRow()
        self.ui.grd_list.takeItem(row)
        self.fn_saveList()
        
    # 리스트 행 복사
    def fn_copyList(self) :
        self.fn_editEndList()
        
        copyText = self.ui.grd_list.currentItem().text()
        clipboard.copy(copyText)
        self.fn_toast("복사 성공")
        
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
    app.setStyleSheet(customStyle.style_sheet)
    
    window = MainWindow()        
    window.show()                 
    sys.exit(app.exec())         
   