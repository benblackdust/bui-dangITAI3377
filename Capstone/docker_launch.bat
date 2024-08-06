@echo off
setlocal

:: Get the current path
set "currentPath=%~dp0"

:: Remove the trailing backslash if there is one
set "currentPath=%currentPath:~0,-1%"

echo "Current path: %currentPath%"

:: Ask the user if they want to rebuild the Docker container
set /p rebuild="Do you want to rebuild the Docker container? (Y/N): "
if /i "%rebuild%"=="Y" (
    docker build . -t capstone
)

:: Run the Docker container with the dynamic path
docker run -it --rm --gpus=all -p 8888:8888 -p 5000:5000 -v "%currentPath%\notebooks:/root/notebooks" capstone

endlocal
