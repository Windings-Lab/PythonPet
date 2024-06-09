@echo off
set PATH_TO_VENV=D:\Programming\Python\pythonProject\venv
set COMPILE_FILE=addressbook.proto

call %PATH_TO_VENV%\Scripts\activate.bat
protoc -I=./src --python_out=./out --pyi_out=./out %COMPILE_FILE%
echo Compiled %COMPILE_FILE%
pause