@echo off
chcp 65001 >nul
title Privet AI Editor
cd /d "%~dp0.."
start "" http://localhost:8765/editor_v4.3.html
python -m http.server 8765
pause
