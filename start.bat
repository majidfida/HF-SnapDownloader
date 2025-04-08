@echo off
REM ========================================================
REM Start Batch File:
REM This script activates the virtual environment and then
REM runs the Download_Models.py script.
REM ========================================================

echo Activating virtual environment...
call venv\Scripts\activate

echo Starting Download_Models.py...
python Download_Models.py

pause
