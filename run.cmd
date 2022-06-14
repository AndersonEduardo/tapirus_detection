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
if errorlevel 1 goto NOPYTHON
echo.
echo STATUS: ...Python is successfully installed and running in your system.
echo.
goto INSTALLPACKAGES

::instalando pacotes
:INSTALLPACKAGES
echo.
echo STATUS: Checking for python packages...
echo.
pip3 install -r requirements.txt
if errorlevel 1 goto PIPERROR
echo.
echo STATUS: ...packages are Ok.
echo.
goto RUNID

::erro python
:NOPYTHON
echo.
echo STATUS: Python not found. Make sure it is installed and you are using Anaconda Prompt to run this program.
echo.
goto END

::erro no pip install
:PIPERROR
echo.
echo STATUS: Failure in installing python packages.
echo.
goto END

::rodando analise dos arquivos
:RUNID
echo.
echo STATUS: Analysing files...
echo.
echo python tapirus_detection.py %par_a% %par_b%
python tapirus_detection.py %par_a% %par_b%
if errorlevel 1 goto ANALYSISERROR
echo.
echo STATUS: ...files analysis completed.
echo.

:ANALYSISERROR
echo.
echo STATUS: Failure running analysis.
echo.
goto END

:: fechamento
:END
echo.
echo ----------------------------------------------------
echo             ## Execução finalizada! ##
echo ----------------------------------------------------
echo.
