# Приватный ИИ-редактор текста

Приватный ИИ-редактор, который работает **целиком на твоём устройстве**. Без
облака, без аккаунта, без отправки данных на сервер. Сокращение, перефраз,
перевод, анонимизация и правка грамматики через локальную модель (LM Studio)
или прямо в браузере через transformers.js.

## Возможности
- **Сократить / Перефразировать / Перевести / Анонимизировать / Исправить**
  — всё локально.
- **Режим локальной модели** — подключается к LM Studio (или Ollama / llama.cpp)
  через OpenAI-совместимый API на `http://127.0.0.1:1234/v1`.
- **Браузерный режим** — грузит модель через transformers.js (WebGPU или CPU),
  ничего ставить не надо.
- **Приватность** — текст не покидает твой компьютер.

## Быстрый старт

### Вариант А — LM Studio (проще всего)
1. Установи [LM Studio](https://lmstudio.ai), скачай модель (напр. `qwen2.5-0.5b`).
2. В LM Studio: **Local Server → Start Server**, включи **CORS** (Server Settings).
3. Открой `editor_v4.3.html` (двойной клик) → вкладка **«Мой LM Studio»** →
   **Загрузить список**.
4. Выбери модель, вставь текст, нажми **Запустить**.

### Вариант Б — локальный сервер (браузерный режим)
Из папки с `editor_v4.3.html`:
- **Windows:** запусти `launchers/start.bat`
- **Linux/macOS:** запусти `launchers/start.sh` или `launchers/start.command`
- Или везде: `python3 -m http.server 8765`, затем открой
  `http://localhost:8765/editor_v4.3.html`

> Браузерный режим НЕ запускается из `file://` — нужен локальный сервер
> или LM Studio.

## Ссылки
- 🌐 Демо: https://toptestsoft.github.io/privat-ai-editor/
- 🤗 HF Space: https://huggingface.co/spaces/toptestsoft/privat-ai-editor
- 📦 Исходник: https://github.com/toptestsoft/privat-ai-editor

## Лицензия
MIT — см. [LICENSE](LICENSE).
