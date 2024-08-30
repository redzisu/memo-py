# memo-py
Simple Memo app using PySide6.  
- Create, copy, edit, and delete notes.
- Double-click to quickly edit the note.
- To keep the window always on top.
- Developed for practicing PySide6.

| Default | Edit |
|---|---|
![image](https://github.com/user-attachments/assets/e41dd036-8f6a-4d54-9da9-66698eee7d1d) | ![image](https://github.com/user-attachments/assets/60fa2d6e-4cc1-4c21-aa2e-f6b4741a2d53)
   
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
