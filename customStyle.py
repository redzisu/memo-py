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
    
    /* 텍스트편집창 */ 
    QTextEdit {
        padding: 5px 10px;
        border: 1px solid #62A668;  /* 초록색 5px 테두리 */
        color: #000000; /* 기본 텍스트 색상 */
        background-color: #FFFFF2; /* 기본 배경 색상 */
    }

    /* 버튼 */
    QPushButton.custom {
        font-weight: bold;
        border-radius: 5px;
        padding: 5px 10px;
        border: 2px solid transparent;
        color: #FFFFFF;
        background-color: #E7F4F9;
        position: relative;
    }
    QPushButton.custom.btn-blue {
        background-color: #4EC0E9;
        border-color: #4EC0E9;
    }

    QPushButton.custom.btn-blue:hover {
        background-color: #38a2d3;
    }

    QPushButton.custom.btn-blue:pressed {
        background-color: #2c8ab0;
    }

    QPushButton.custom.btn-blue:disabled {
        background-color: #b3e0f2;
        border-color: #b3e0f2;
    }

    QPushButton.custom.btn-grey {
        background-color: #6c757d;
        border-color: #6c757d;
    }

    QPushButton.custom.btn-grey:hover {
        background-color: #5a6268;
    }

    QPushButton.custom.btn-grey:pressed {
        background-color: #4e555b;
    }

    QPushButton.custom.btn-grey:disabled {
        background-color: #e2e6ea;
        border-color: #e2e6ea;
    }

    QPushButton.custom.btn-green {
        background-color: #28a745;
        border-color: #28a745;
    }

    QPushButton.custom.btn-green:hover {
        background-color: #218838;
    }

    QPushButton.custom.btn-green:pressed {
        background-color: #1e7e34;
    }

    QPushButton.custom.btn-green:disabled {
        background-color: #c3e6cb;
        border-color: #c3e6cb;
    }

    QPushButton.custom.btn-yellow {
        background-color: #ffc107;
        border-color: #ffc107;
    }

    QPushButton.custom.btn-yellow:hover {
        background-color: #e0a800;
    }

    QPushButton.custom.btn-yellow:pressed {
        background-color: #d39e00;
    }

    QPushButton.custom.btn-yellow:disabled {
        background-color: #ffeeba;
        border-color: #ffeeba;
    }

    QPushButton.custom.btn-red {
        background-color: #dc3545;
        border-color: #dc3545;
    }

    QPushButton.custom.btn-red:hover {
        background-color: #c82333;
    }

    QPushButton.custom.btn-red:pressed {
        background-color: #bd2130;
    }

    QPushButton.custom.btn-red:disabled {
        background-color: #f5c6cb;
        border-color: #f5c6cb;
    }
"""