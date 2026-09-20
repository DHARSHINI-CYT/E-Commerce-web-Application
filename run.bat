@echo off
echo ==========================================
echo LUXESTORE E-Commerce Application
echo Backend: Python (Django) + SQLite
echo Frontend: HTML/CSS/JavaScript (React)
echo ==========================================

REM Check if Python is installed
python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed or not added to PATH. Please install Python.
    pause
    exit /b
)

echo Installing Django...
pip install django

echo.
echo Running Database Migrations...
python manage.py makemigrations api
python manage.py migrate

echo.
echo Seeding Database with Mock Products...
python seed.py

echo.
echo Starting LUXESTORE Server...
echo The application will open in your browser shortly!
start http://127.0.0.1:8000
python manage.py runserver
