@echo off
echo Processing SVG file: %1

:: Check if a file was dropped
if "%~1"=="" (
    echo Error: No file provided.
    echo Please drag and drop an SVG file onto this script.
    goto :pause_exit
)

:: Check if the dropped file is an SVG
if /I not "%~x1"==".svg" (
   echo Error: The dropped file is not an SVG file (%~x1^).
   echo Please drop a file with the .svg extension.
   goto :pause_exit
)

:: Construct the output path: same directory, same name, .png extension
:: %~dpn1 expands to Drive:\Path\Filename (without extension) of the first argument (%1)
set OUTPUT_PNG_PATH=%~dpn1.png
echo Output PNG will be: %OUTPUT_PNG_PATH%

:: Construct the full path to the Python script
:: %~dp0 expands to the Drive:\Path\ of the directory containing this batch file
set PYTHON_SCRIPT_PATH=%~dp0convert_svg_arg.py
echo Running Python script: %PYTHON_SCRIPT_PATH%

:: Check if the Python script exists where the batch file is
if not exist "%PYTHON_SCRIPT_PATH%" (
    echo Error: Python script 'convert_svg_arg.py' not found in the same directory as this batch file.
    echo Make sure both files are saved together.
    goto :pause_exit
)

:: --- Execute the Python script ---
:: Use quotes around paths to handle spaces
python "%PYTHON_SCRIPT_PATH%" "%1" "%OUTPUT_PNG_PATH%"

:: Check if Python command failed (optional but good practice)
if errorlevel 1 (
    echo.
    echo ************************************************
    echo * An error occurred during Python execution.   *
    echo * Check messages above.                        *
    echo * Ensure Python is installed and in PATH.      *
    echo * Ensure CairoSVG is installed (pip install CairoSVG). *
    echo * You may need GTK+ runtime on Windows.        *
    echo ************************************************
)

:pause_exit
echo.
pause