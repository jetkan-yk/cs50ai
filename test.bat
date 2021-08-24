setlocal ENABLEDELAYEDEXPANSION

@echo off
for /d /r %%d in (*) do (
    cd %%d
    if exist *_test.py (
        pytest 
        if !errorlevel! eq 1 exit 1
    )
)