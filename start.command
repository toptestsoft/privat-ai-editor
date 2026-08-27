#!/bin/bash
cd "$(dirname "$0")"
(sleep 1.5 && open http://localhost:8765/index.html) &
python3 -m http.server 8765
