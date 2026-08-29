# FAQ — Приватный ИИ-редактор текста (RU)

**В: Текст уходит с моего устройства?**
A: Нет. В режиме LM Studio модель крутится локально. В браузерном режиме модель
грузится в браузер через WebGPU/CPU. Ничего не загружается в облако.

**В: «Failed to fetch» при подключении к LM Studio**
A: Сервер LM Studio не запущен или выключен CORS. В LM Studio: Local Server →
Start Server, затем Settings → Server Settings → включи CORS.

**В: «Cannot run from file://»**
A: Браузерный режим требует локальный сервер. Запусти `launchers/start.bat`
(Windows) или `launchers/start.sh` (Linux/macOS), либо `python3 -m http.server 8765`
и открой `http://localhost:8765/editor_v4.3.html`. Вкладка LM Studio работает
из file://.

**В: «WebGPU not available»**
A: Браузер/железо не поддерживает WebGPU. Приложение переключится на CPU
(медленнее). Или используй режим LM Studio.

**В: Какую модель выбрать?**
A: Для браузера начни с `Qwen 2.5 0.5B` (хороший русский, ~1 ГБ). Для LM Studio
подойдёт любая локальная модель (gemma-4-e4b-it, qwen3.x и др.).

**В: Модель выдаёт 404 на Hugging Face**
A: У некоторых ONNX-моделей нестандартные имена файлов. Выбери другую из списка
(`Qwen 2.5 0.5B` точно работает).
