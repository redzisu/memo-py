style_sheet = """
    QMainWindow {
        background-color: white;  /* 창 배경색 */
    }
    
    /* 리스트 */ 
    QListWidget {
        border-top: 3px double #CACACA;
        border-bottom: 3px double #CACACA;
        border-left: none;
        border-right: none;
        outline: none; /* 아이템 선택했을 때 점 테두리 제거 */
    }
    
    QListWidget::item {
        padding: 10px;
        border-bottom: 1px dashed #CACACA;  /* 아이템 아래쪽 회색 1px 테두리 */
    }
    
    QListWidget::item:hover {
        background-color: #F1F1F1;  /* 회색 배경 */
    }
    
    QListWidget::item:selected {
        background-color: #E7F4F9;  /* 하늘색 배경 */
        color: black;
        border-left: 5px solid #62A668;  /* 초록색 5px 테두리 */
    }
    
    /* 버튼 */
    QPushButton {
        background-color: #62A668;  /* 초록색 배경 */
        color: white;  /* 흰색 텍스트 */
        padding: 4px 16px;  /* 패딩 */
        border-radius: 4px;  /* 둥근 모서리 */
    }
    
    QPushButton:hover {
        background-color: #57945D;  /* 조금 더 어두운 초록색 배경 */
    }
    
    QPushButton:pressed {
        background-color: #4E8454;  /* 더 어두운 초록색 배경 */
    }
    
    QPushButton:disabled {
        background-color: #D3D3D3;  /* 비활성화된 버튼 배경색 */
        color: #A0A0A0;  /* 비활성화된 버튼 텍스트 색상 */
        border: 2px solid #CACACA;  /* 비활성화된 버튼 테두리 */
    }
    
"""