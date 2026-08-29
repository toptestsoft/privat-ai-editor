@echo off
chcp 65001 >nul
title Privet AI Editor
start "" http://localhost:8000/index.html
python -m http.server 8000
pause
