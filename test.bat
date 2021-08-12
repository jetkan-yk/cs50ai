@echo off
for /d /r %%d in (*) do (
    cd %%d
    if exist *_test.py pytest
)