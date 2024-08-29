# memo-py
Simple Memo app using PySide6.  
- Create, edit, and delete notes.
- Double-click to quickly copy the note.
- Developed for practicing PySide6.

| Default | Edit |
|---|---|
![image](https://github.com/user-attachments/assets/b0d056a2-502a-4ff8-b2ee-36ea406bf624) | ![image](https://github.com/user-attachments/assets/1cca1b12-ac4d-4205-9cd6-5e1a0e97d941)
   
## Environment 
- Python v3.12
  
| Package | Installation Command | 
|--|--|
| [PySide6](https://pypi.org/project/PySide6/) | `pip install PySide6` | 
| [clipboard](https://pypi.org/project/clipboard/)  | `pip install clipboard` |
| [pyqttoast](https://pypi.org/project/pyqt-toast-notification/)  | `pip install pyqt-toast-notification` |

To edit the UI, enter `pyside-designer` into the command line. It is included with the pyside6 package.

## Data Storage
The data is saved as a `pickle` file in the **Documents** folder.   

![image](https://github.com/user-attachments/assets/f266ca19-304e-4a31-9f2f-53cff19148a2)  
*⚠️  Please make sure not to delete this backup file.*

## Build
1. Download the source code from the repository.
2. Package the project by running the following command:
```bash
pyinstaller main.spec
```

## Run
1. Navigate to the `dist` folder.
2. Download `Memo.exe`.
3. double-click to run the app.

## Planned Features
- [x] 창 크기에 따라 컴포넌트 사이즈를 유연하게 조정 `2024.08.02`
- [x] 예쁜 아이콘 적용 `2024.08.29`
- [ ] 키보드 단축키를 통한 편집 지원
- [ ] 즐겨찾기 기능 추가
- [ ] 정렬 기능 구현
- [ ] 날짜 데이터 및 테이블 형식 지원
- [ ] 메모 데이터를 엑셀 파일로 출력
- [ ] 체크박스를 이용한 다건 삭제 기능
- [ ] 윈도우가 다크모드이면 그리드 배경도 검정색이 되는 오류
- [ ] 데이터베이스 사용방식 변경 (pickle -> sqlite3)

