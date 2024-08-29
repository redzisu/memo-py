import sys
import os
import clipboard
import pickle
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from pyqttoast import Toast, ToastPreset
from view_ui import Ui_View
import styles

class TextEditDelegate(QStyledItemDelegate):
    def __init__(self, list_widget, main_window, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.list_widget = list_widget
        self.main_window = main_window
        
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
        
        if option.state & QStyle.State_Selected: #or option.state & QStyle.State_MouseOver:
            rect = option.rect
            icon_size = QSize(20, 20) 
        
            copy_rect = QRect(rect.right() - 60, rect.top() + 8, icon_size.width(), icon_size.height())
            delete_rect = QRect(rect.right() - 25, rect.top() + 8, icon_size.width(), icon_size.height())

            copy_icon = QIcon("./icon/copy.png")
            delete_icon = QIcon("./icon/delete.png")

            copy_icon.paint(painter, copy_rect, Qt.AlignCenter)
            delete_icon.paint(painter, delete_rect, Qt.AlignCenter)
    
    def editorEvent(self, event, model, option, index):
        if event.type() == QMouseEvent.MouseButtonRelease:
            pos = event.position().toPoint()
            item = self.list_widget.itemAt(pos)
            
            icon_size = QSize(20, 20) 
            
            if item:
                rect = self.list_widget.visualItemRect(item)
                copy_rect = QRect(rect.right() - 60, rect.top(), icon_size.width(), icon_size.height())
                delete_rect = QRect(rect.right() - 25, rect.top(), icon_size.width(), icon_size.height())

                if copy_rect.contains(pos):
                    self.main_window.fn_copyList()
                    return True

                if delete_rect.contains(pos):
                    self.main_window.fn_confirm(
                    "삭제하시겠습니까?", 
                    lambda: self.main_window.fn_deleteList(), 
                    lambda: None
                    )
                    return True

        return super().editorEvent(event, model, option, index)
    
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        
        self.ui = Ui_View()
        self.ui.setupUi(self)
        
        self.setWindowTitle("Memo")
        self.setWindowIcon(QIcon.fromTheme("edit-paste")) 

        Toast.setPositionRelativeToWidget(self) # Toast를 부모창에 종속된 위치로 변경
        Toast.setOffset(10, 10)
        
        
        #==================  Default Setting  ====================
        # QListWidget 커스텀 텍스트 편집 
        self.ui.grd_list.setItemDelegate(TextEditDelegate(self.ui.grd_list, self))
        
        # QListWidget 데이터 불러오기
        self.pickle_file_path = self.resource_path('MemoBackup.pickle')
        
        if os.path.exists(self.pickle_file_path):
            with open(self.pickle_file_path, "rb") as f: # rb : 바이트 형식으로 읽어오기
                data = pickle.load(f) 
            self.ui.grd_list.insertItems(0, data)
        else:
            with open(self.pickle_file_path, "wb") as f: # wb : 바이트 형식으로 쓰기
                pickle.dump('', f) 
            self.fn_alert("[신규생성] 백업 파일이 존재하지 않습니다.")
            
        # 버튼 css 설정
        self.ui.btn_insertList.setProperty("class", "custom btn-green") 
        self.ui.btn_insertList.setIconSize(QSize(20, 20))  # 아이콘 크기 설정
        self.ui.btn_insertList.setIcon(QIcon("./icon/add.png"))
        
        self.ui.btn_topWindow.setProperty("class", "transparent") 
        self.ui.btn_topWindow.setIconSize(QSize(20, 20))  # 아이콘 크기 설정
        self.ui.btn_topWindow.setIcon(QIcon("./icon/pin_unFixed.png"))
        
        #==================  Signal  ====================
        self.ui.btn_insertList.clicked.connect(self.fn_insertList)
        self.ui.grd_list.itemClicked.connect(self.fn_editEndList)
        self.ui.grd_list.itemDoubleClicked.connect(self.fn_editList)
        self.ui.grd_list.keyPressEvent = self.event_keyPress
        self.ui.btn_topWindow.clicked.connect(self.fn_toggleOnTop)
        self.is_always_on_top = False
        
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
        
        with open(self.pickle_file_path, "wb") as f: # wb : 바이트 형식으로 쓰기
            pickle.dump(itemData, f) 
            
    # 리스트 keyPress 이벤트
    def event_keyPress(self, event):
        if event.key() == Qt.Key_Return and event.modifiers() & Qt.ControlModifier:
            self.fn_editEndList()
        else:
            super().keyPressEvent(event)  # 기본 동작 처리
            
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
        try:
            self.fn_toast("복사 성공")
        except Exception as e:
            print("ddddd" )
        
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
        try:
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
        except Exception as e:
            print("An error occurred in show_toast:", e)
    
    def fn_toggleOnTop(self, pStr):
        base_flags = Qt.Window | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint
        if self.is_always_on_top:
            self.setWindowFlags(base_flags)
            self.is_always_on_top = False
            
            self.ui.btn_topWindow.setIcon(QIcon("./icon/pin_unFixed.png"))
            
        else:
            self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)
            self.is_always_on_top = True
            
            self.ui.btn_topWindow.setIcon(QIcon("./icon/pin_fixed.png"))
            
        self.show()
    
    # pickle파일 빌드용
    def resource_path(self, relative_path):
        try:
            base_path = os.path.expandvars(r'%USERPROFILE%\Documents') # 문서
        except AttributeError:
            base_path = os.path.dirname(os.path.abspath(__file__))
            
        # 폴더생성
        os.makedirs(base_path + '\Memo.bak', exist_ok=True)
        return os.path.join(base_path + '\Memo.bak', relative_path)
        
if __name__ == "__main__":
    app = QApplication(sys.argv) 
    app.setStyleSheet(styles.style_sheet)
    
    window = MainWindow()        
    window.show()                 
    sys.exit(app.exec())         
   