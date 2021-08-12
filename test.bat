setlocal ENABLEDELAYEDEXPANSION

@echo off
for /d /r %%d in (*) do (
    cd %%d
    if exist *_test.py (
        pytest 
        if !errorlevel! neq 0 exit /b 1
    )
)