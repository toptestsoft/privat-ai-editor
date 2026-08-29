# FAQ — Private AI Text Editor (EN)

**Q: Does my text leave my device?**
A: No. In LM Studio mode the model runs locally. In browser mode the model
runs in your browser via WebGPU/CPU. Nothing is uploaded.

**Q: "Failed to fetch" when connecting to LM Studio**
A: LM Studio server is not running, or CORS is off. In LM Studio: Local Server
→ Start Server, then Settings → Server Settings → enable CORS.

**Q: "Cannot run from file://"**
A: Browser mode needs a local server. Run `launchers/start.bat` (Windows) or
`launchers/start.sh` (Linux/macOS), or `python3 -m http.server 8765` and open
`http://localhost:8765/editor_v4.3.html`. The LM Studio tab works from file://.

**Q: "WebGPU not available"**
A: Your browser/device lacks WebGPU. The app falls back to CPU (slower). Or use
LM Studio mode.

**Q: Which model should I pick?**
A: For browser mode start with `Qwen 2.5 0.5B` (good Russian, ~1 GB). For LM
Studio mode any local model works (gemma-4-e4b-it, qwen3.x, etc.).

**Q: A model shows 404 on Hugging Face**
A: Some ONNX models have non-standard file names. Pick another from the list
(Qwen 2.5 0.5B is verified working).
