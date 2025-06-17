
pyinstaller --noconfirm --windowed --onefile --name mochi src/mochi/main.py

rmdir /s /q build
del /f mochi.spec
move dist\mochi.exe .\
rmdir /s /q dist