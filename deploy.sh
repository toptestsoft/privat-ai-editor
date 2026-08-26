#!/usr/bin/env bash
# Деплой приватного ИИ-редактора на GitHub Pages (бесплатно, навсегда).
# Запуск:  bash deploy.sh
# Перед запуском создай пустой ПУБЛИЧНЫЙ репозиторий toptestsoft/privat-ai-editor на github.com
# (через веб: https://github.com/new ). Скрипт сам запушит и настроит gh-pages.
#
# При первом push git спросит логин/пароль (или токен) — введи свой.

set -e
REPO="toptestsoft/privat-ai-editor"
ROOT="$(cd "$(dirname "$0")" && pwd)"

cd "$ROOT"

# 1) Пуш основной ветки main
git branch -M main
git remote remove origin 2>/dev/null || true
git remote add origin "https://github.com/${REPO}.git"
echo ">>> Пуш в main (введи логин/токен при запросе):"
git push -u origin main

# 2) Пуш папки deploy/ в ветку gh-pages (источник для GitHub Pages)
echo ">>> Пуш deploy/ в gh-pages:"
git subtree push --prefix deploy origin gh-pages

echo
echo "ГОТОВО. Теперь зайди в репозиторий:"
echo "  https://github.com/${REPO}/settings/pages"
echo "  Source: Deploy from a branch -> gh-pages -> /root -> Save"
echo
echo "Через ~1 минуту сайт будет тут:"
echo "  https://${REPO%/*}.github.io/${REPO#*/}/"
