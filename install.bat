@echo off
REM ========================================================
REM Installer Batch File:
REM This script sets up an isolated virtual environment,
REM installs required dependencies, and then launches the
REM start.bat file.
REM ========================================================

REM Check if the virtual environment folder "venv" exists; if not, create it.
if not exist "venv\Scripts\activate" (
    echo Creating virtual environment...
    python -m venv venv
)

echo Activating virtual environment...
call venv\Scripts\activate

echo Upgrading pip...
python -m pip install --upgrade pip

echo Installing required packages: huggingface_hub and hf_transfer...
pip install huggingface_hub hf_transfer

echo Virtual environment setup complete.
echo.
echo Launching the application using start.bat...
call start.bat

pause
