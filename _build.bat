@echo off
title DL2PFU Builder
color 0c

:main
cls
echo Press any key to build the executable...
pause>nul
echo.
pyinstaller -F --icon=icon.ico -n DL2-PAKFile-Utility main.py
echo.
echo Build Complete!
echo.
pause

:cleanup
cls
echo Cleaning up...
echo.
del /s DL2-PAKFile-Utility.spec>NUL
rmdir /S /Q "build"
rmdir /S /Q "__pycache__"
echo Deleted .spec File, 'build' Directory, and '__pycache__' Directory!
echo.
pause
color
