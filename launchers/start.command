#!/bin/bash
cd "$(dirname "$0")"
cd "$(dirname "$0")/.."
(sleep 1.5 && open http://localhost:8765/editor_v4.3.html) &
python3 -m http.server 8765
