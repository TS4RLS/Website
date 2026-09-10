@echo off
REM TS4RLS Website - Local dev server (Windows)
REM Usage: dev-server.bat [port] [--no-dev-mode]
REM   port            default: 8000
REM   --no-dev-mode   fetch Engine content from GitHub instead of the local
REM                   sibling checkout (production behavior) for this run
REM
REM DEV_MODE is forced ON for every run of this script - it reveals the
REM dev-mode banner and (once there's a script that reads it) makes local
REM content come from the sibling checkout next to this one (..\Engine)
REM instead of GitHub, so local edits show up here without pushing first.
REM Pass --no-dev-mode to test the site as it behaves in production instead.
setlocal
set "DIR=%~dp0"

where python >nul 2>nul
if errorlevel 1 (
    where py >nul 2>nul
    if errorlevel 1 (
        echo Python 3 is required to run dev-server.py
        exit /b 1
    )
    py "%DIR%dev-server.py" %*
) else (
    python "%DIR%dev-server.py" %*
)
