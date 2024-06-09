@echo off
set PATH_TO_VENV=D:\Programming\Python\pythonProject\venv
set SRC_DIR=./src
set OUT_DIR=./out
set COMPILE_FILE=addressbook.proto

call %PATH_TO_VENV%\Scripts\activate.bat
rem protoc -I=%SRC_DIR% --python_out=%OUT_DIR% --pyi_out=%OUT_DIR% %COMPILE_FILE%
python -m grpc_tools.protoc -I=%SRC_DIR% --python_out=%OUT_DIR% --pyi_out=%OUT_DIR% --grpc_python_out=%OUT_DIR% %COMPILE_FILE%
echo Compiled %COMPILE_FILE% proto and gRPC
pause