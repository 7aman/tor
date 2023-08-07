@echo off

if "%~1"=="" goto default
if "%~1"=="s" goto snowflake
if "%~1"=="sf" goto snowflake
if "%~1"=="snow" goto snowflake
if "%~1"=="snowflake" goto snowflake
if "%~1"=="m" goto meek
if "%~1"=="mk" goto meek
if "%~1"=="meek" goto meek
if "%~1"=="o" goto obfs4
if "%~1"=="ob" goto obfs4
if "%~1"=="obfs4" goto obfs4
if "%~1"=="clean" goto clean
if "%~1"=="new" goto identity
EXIT /B 0

:default
goto obfs4

:obfs4
CALL :kill_existing
C:\Tor\tor.exe -f obfs4.txt
EXIT /B 0

:meek
CALL :kill_existing
C:\Tor\tor.exe -f meek.txt
EXIT /B 0

:snowflake
CALL :kill_existing
C:\Tor\tor.exe -f snowflake.txt
EXIT /B 0

:kill_existing
taskkill.exe /F /IM Tor.exe 2> nul
mkdir Data 2> nul
EXIT /B 0

:clean
echo Data folder is cleaned
taskkill.exe /F /IM Tor.exe 2> nul
if exist Data (rmdir /s/q Data 2> nul)
mkdir Data 2> nul
TIMEOUT /nobreak /t 5
EXIT /B 0

:identity
echo change to a new identity
C:\Tor\torch.exe
EXIT /B 0
