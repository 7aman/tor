@echo off
cd /d %~dp0
pyinstaller --clean --onefile --console --icon ..\\files\\icon.ico --distpath ..\\tor torch.py
