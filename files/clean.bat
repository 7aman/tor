@echo off
taskkill.exe /F /IM Tor.exe 2> nul
if exist Data (rmdir /s/q Data 2> nul)
mkdir Data 2> nul

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

:default
goto obfs4

:obfs4
C:\Tor\tor.exe -f obfs4.txt

:meek
C:\Tor\tor.exe -f meek.txt

:snowflake
C:\Tor\tor.exe -f snowflake.txt
