setlocal ENABLEDELAYEDEXPANSION

@echo off
for /d /r %%d in (*) do (
    cd %%d
    if exist *_test.py (
        pytest 
        if !errorlevel! equ 1 exit 1
    )
)