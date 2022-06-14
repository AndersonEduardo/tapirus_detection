@echo off

::variaveis
set par_a=%1
set par_b=%2

:: abertura
echo.
echo.
echo -----------------------------------------
echo    ## Running Tapir Detection Bot ###
echo                (%date%)
echo -----------------------------------------
echo.
echo.
pause
goto PYTHONCHECK 

:: checagem da instalacao do python
:PYTHONCHECK
echo.
echo STATUS: Checking for Python in your system...
echo.
python.exe --version >NUL 2>&1
if errorlevel 1 goto nopython
echo.
echo STATUS: ...Python is successfully installed and running in your system.
echo.
goto RUNID

::erro python
:NOPYTHON
echo.
echo STATUS: python not found. Make sure it is installed and you are using Anaconda Prompt to run this program.
echo.
goto end

::rodando analise dos arquivos
:RUNID
echo.
echo STATUS: Analysing files...
echo.
echo python tapirus_detection.py %par_a% %par_b%
python tapirus_detection.py %par_a% %par_b%

:: fechamento
:END
echo.
echo ----------------------------------------------------
echo             ## Execução finalizada! ##
echo ----------------------------------------------------
echo.
