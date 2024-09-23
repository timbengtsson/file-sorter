@echo off

:: Check for administrator rights
net session >nul 2>&1
if %errorlevel% neq 0 (
    echo Requesting administrator privileges...
    powershell -command "Start-Process '%~f0' -Verb runAs"
    exit /b
)

:: Check if task exist
schtasks /query /tn "SortFilesLikeABoss" >nul 2>&1

:: And delete task if exists = errorlevel = 0 (no error task exist)
if %errorlevel%==0 (
    echo SortFilesLikeABoss task existed. Removing it.
    schtasks /delete /tn "SortFilesLikeABoss" /f
) else (
    echo SortFilesLikeABoss task does not exist yet. Nothing to do here. Keep calm and carry on.
)

:: Print message for 5 sekconds, then close cmd window
timeout /t 5 /nobreak >nul

exit