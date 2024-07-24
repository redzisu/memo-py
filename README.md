# memo-pyside6
Simple Memo app using Pyside6.  
- Create, edit, and delete notes.
- Double-click to quickly copy the note.
- Developed for practicing PySide6.

|**Default** | **Edit** |
|---|---|
![image](https://github.com/user-attachments/assets/b0d056a2-502a-4ff8-b2ee-36ea406bf624) | ![image](https://github.com/user-attachments/assets/1cca1b12-ac4d-4205-9cd6-5e1a0e97d941)
   
## Use
- Python
- PySide6, Qt Designer

## Library
- `import pickle`
- `import clipboard`
- `import pyqttoast`

## Data
The data is saved as a `pickle` file in the _Documents_ folder.  

![image](https://github.com/user-attachments/assets/f266ca19-304e-4a31-9f2f-53cff19148a2)

⚠️  Please make sure not to delete this backup file.

## Run
1. Navigate to the `dist` folder.
2. Download `Memo.exe`.
3. double-click to run the app.

#### OR
1. Download the source code from the repository.
2. Package the project by running the following command:
```bash
pyinstaller main.spec
```

## Planned Features
- 창 크기에 따라 컴포넌트 사이즈를 유연하게 조정
- 즐겨찾기 기능 추가
- 정렬 기능 구현
- 날짜 데이터 및 테이블 형식 지원
- 메모 데이터를 엑셀 파일로 출력
- 아이콘 사용자 맞춤 수정 가능
- 체크박스를 이용한 다건 삭제 기능
- 키보드 단축키를 통한 편집 지원
- 10글자 이내는 행 높이에 맞춰 조정하고, 10글자 이상은 힌트를 표시하며 창의 1/3 크기로 설정
- 마크다운 형식 입력 시 해당 스타일로 렌더링
