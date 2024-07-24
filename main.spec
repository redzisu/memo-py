# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all

# 'pyqttoast' 패키지의 모든 파일을 수집
datas, binaries, hiddenimports = collect_all('pyqttoast')

a = Analysis(
    ['main.py'],
    pathex=['.'],
    binaries=binaries,  # 수집된 바이너리 파일 포함
    datas=datas,        # 수집된 데이터 파일 포함
    hiddenimports=hiddenimports,  # 숨겨진 모듈 포함
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Memo',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
