set PY_PATH=.\dlls
set PATH=%PATH%;%PY_PATH%

chcp 65001 > Nul

.\Python27\python.exe .\proj\test\test_event.py

pause
