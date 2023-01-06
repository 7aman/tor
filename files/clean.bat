@echo off
taskkill.exe /F /IM Tor.exe 2> nul
if exist Data (rmdir /s/q Data 2> nul)
mkdir Data 2> nul
C:\Tor\tor.exe -f config.txt
