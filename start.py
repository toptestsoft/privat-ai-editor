#!/usr/bin/env python3
import http.server,socketserver,webbrowser,os,time,threading
PORT=8765;DIR=os.path.dirname(os.path.abspath(__file__))
os.chdir(DIR)
threading.Thread(target=lambda:(time.sleep(1.5),webbrowser.open(f"http://localhost:{PORT}/index.html")),daemon=True).start()
print(f"\n  🔒 http://localhost:{PORT} · Ctrl+C — стоп\n")
with socketserver.TCPServer(("",PORT),http.server.SimpleHTTPRequestHandler) as h:
    try:h.serve_forever()
    except KeyboardInterrupt:print("\n  ⏹ Остановлено.")
