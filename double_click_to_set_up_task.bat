@echo off

:: Crrent dir 
set "PROJECT_PATH=%~dp0"

:: Define the path to the venv and the Python script
set "VENV_PATH=%PROJECT_PATH%venv"
set "SCRIPT_PATH=%PROJECT_PATH%main.py"

:: Check for administrator rights
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo Requesting administrator privileges...
    powershell -command "Start-Process '%~f0' -Verb runAs"
    exit /b
)

where python >nul 2>&1
if %errorlevel%==0 (
    echo Python is installed.
    python --version
) else (
    echo Python is not installed. ...Need Python. 
    exit /b
)
 
:: create venv if not exiswt
if not exist "%VENV_PATH%" ( 
    echo No virtual python environment exists. Creating it...
    python -m venv "%VENV_PATH%" 
) 

:: activate it
echo Activating virtual environment...
call "%VENV_PATH%/Scripts/activate.bat"

:: install dependencies if it exiss
if exist "%PROJECT_PATH%rewqurequirements.txt" ( 
    echo Installing packages...
    pip install -r "%PROJECT_PATH%requirements.txt"
)

:: Check if task exist
schtasks /query /tn "SortFilesLikeABoss" >nul 2>&1
:: And delete task if exists = errorlevel = 0 (no error task exist)
if %errorlevel%==0 (
    echo SortFilesLikeABoss task aready existed. Removing it.
    schtasks /delete /tn "SortFilesLikeABoss" /f
)

:: Schedule a task that runs every 10 minutes indefinitely
    :: /create = creeates the scheduled task
    :: /tn = task name 
    :: /tr = The task the schehduled task will perform
    :: /sc minute /mo 10 =
    :: /f = Force creation of the task without waiting for confirmation 
    :: /ru SYSTEM = run quietly in the background. (else a comand prompt will flash open)
schtasks /create /tn "SortFilesLikeABoss" /tr "\"%VENV_PATH%\Scripts\python.exe\" \"%SCRIPT_PATH%\"" /sc minute /mo 30 /f /rl highest

echo Task has been setup!
echo.

set /a countdown=10 

:countdown_loop
if %countdown% GEQ 1 (
    echo Closing in %countdown%...
    timeout /t 1 /nobreak >nul 
    set /a countdown-=1
    goto countdown_loop
)

echo Bye!
timeout /t 1 /nobreak >nul

exit