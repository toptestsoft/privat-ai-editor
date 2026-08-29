# Private AI Text Editor

A privacy-focused AI text editor that runs **fully on your device**. No cloud,
no account, no data leaving your machine. Summarize, rephrase, translate,
anonymize, and fix grammar using a local LLM (LM Studio) or directly in the
browser via transformers.js.

## Features
- **Shorten / Rephrase / Translate / Anonymize / Fix grammar** — all local.
- **Local LLM mode** — connects to LM Studio (or Ollama / llama.cpp) via
  OpenAI-compatible API at `http://127.0.0.1:1234/v1`.
- **In-browser mode** — loads a model via transformers.js (WebGPU or CPU),
  no install needed.
- **Privacy** — text never leaves your device.

## Quick start

### Option A — LM Studio (easiest)
1. Install [LM Studio](https://lmstudio.ai), download a model (e.g. `qwen2.5-0.5b`).
2. In LM Studio: **Local Server → Start Server**, enable **CORS** (Server Settings).
3. Open `editor_v4.3.html` (double-click) → tab **"My LM Studio"** → **Load list**.
4. Pick a model, paste text, hit **Run**.

### Option B — Local server (browser mode)
From the folder with `editor_v4.3.html`:
- **Windows:** run `launchers/start.bat`
- **Linux/macOS:** run `launchers/start.sh` or `launchers/start.command`
- Or anywhere: `python3 -m http.server 8765` then open
  `http://localhost:8765/editor_v4.3.html`

> Browser mode does NOT run from `file://` — use a local server or LM Studio.

## Links
- 🌐 Live demo: https://toptestsoft.github.io/privat-ai-editor/
- 🤗 HF Space: https://huggingface.co/spaces/toptestsoft/privat-ai-editor
- 📦 Source: https://github.com/toptestsoft/privat-ai-editor

## License
MIT — see [LICENSE](LICENSE).
