#!/bin/bash
cd "$(dirname "$0")/.."
echo ""
echo "  🔒 Приватный ИИ-редактор текста"
echo "  📡 http://localhost:8765  ·  ⏹ Ctrl+C — стоп"
echo ""
command -v python3 >/dev/null || { echo "❌ Установи: sudo apt install python3"; read -p "Enter..."; exit 1; }
(sleep 1.5 && xdg-open http://localhost:8765/editor_v4.3.html 2>/dev/null) &
python3 -m http.server 8765
