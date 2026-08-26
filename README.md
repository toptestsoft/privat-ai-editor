# Приватный ИИ-редактор текста

Бесплатный универсальный инструмент на локальных ИИ-моделях. Сокращай, перефразируй,
выделяй ключевое и переводи текст — **без отправки данных в облако**.

## Два режима
- **Мой LM Studio** — работает на твоём компьютере через [LM Studio](https://lmstudio.ai)
  (локальный сервер `http://localhost:1234`). Быстро, приватно, без подписок.
  Рекомендуемая модель: `gemma-4-e4b-it` (не-thinking, отвечает по-русски).
  Работает **любой OpenAI-совместимый локальный сервер** — LM Studio, Ollama
  (`http://localhost:11434/v1`), llama.cpp, vLLM, KoboldCpp, text-generation-webui:
  просто поменяй адрес эндпоинта в поле выше.
- **Браузерная модель** — запускает Qwen2.5-0.5B прямо в браузере через transformers.js
  (WebGPU, либо CPU-фолбэк). Работает у любого посетителя, даже без LM Studio.

## Запуск локально (для разработки/теста)
Браузер блокирует прямой fetch к `localhost:1234` (CORS), поэтому используем мини-прокси:
```
cd deploy
python3 serve.py
```
Открыть http://localhost:8080/ → в LM Studio загрузить `gemma-4-e4b-it`, включить Server + CORS.

## Деплой (GitHub Pages, бесплатно навсегда)
1. Создать репозиторий `toptestsoft/privat-ai-editor` (публичный).
2. Запушить содержимое папки `deploy/` в корень + ветку `gh-pages`:
   ```
   git init
   git add -A
   git commit -m "init: приватный ИИ-редактор"
   git branch -M main
   git remote add origin https://github.com/toptestsoft/privat-ai-editor.git
   git push -u origin main
   # для GitHub Pages:
   git subtree push --prefix deploy origin gh-pages
   ```
3. В настройках репозитория: Settings → Pages → Source: `Deploy from a branch` → `gh-pages` → `/root`.
4. Готово: https://toptestsoft.github.io/privat-ai-editor/

## Поддержать автора
- Boosty: https://boosty.to/toptestsoft
- Dalink (донат): https://dalink.to/toptestsoft
- GitHub: https://github.com/toptestsoft
- Hugging Face: https://huggingface.co/toptestsoft
