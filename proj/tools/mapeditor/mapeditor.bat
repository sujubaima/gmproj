set PY_PATH=..\..\..\dlls
set PATH=%PATH%;%PY_PATH%

chcp 65001 > Nul

..\..\..\Python38\python.exe .\editor.py

pause
