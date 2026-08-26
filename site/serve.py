#!/usr/bin/env python3
"""
Локальный прокси-сервер для тестирования приватного ИИ-редактора.
- Отдаёт index.html на http://localhost:8080/
- Проксирует /v1/* -> http://localhost:1234/v1/* (LM Studio)
  под тем же origin, поэтому браузерный fetch НЕ упирается в CORS.

Запуск:  python3 serve.py
Затем открой: http://localhost:8080/
"""
import http.server
import socketserver
import urllib.request
import json

LM_STUDIO = "http://localhost:1234"

class Handler(http.server.BaseHTTPRequestHandler):
    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.end_headers()

    def do_GET(self):
        if self.path.startswith("/v1/"):
            return self._proxy("GET")
        # отдаём страницу
        try:
            with open("index.html", "rb") as f:
                data = f.read()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(data)
        except FileNotFoundError:
            self.send_error(404)

    def do_POST(self):
        if self.path.startswith("/v1/"):
            return self._proxy("POST")
        self.send_error(404)

    def _proxy(self, method):
        length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(length) if length else None
        url = LM_STUDIO + self.path
        req = urllib.request.Request(url, data=body, method=method)
        req.add_header("Content-Type", "application/json")
        try:
            with urllib.request.urlopen(req, timeout=180) as resp:
                data = resp.read()
                self.send_response(resp.status)
                self.send_header("Content-Type", "application/json")
                self._cors()
                self.end_headers()
                self.wfile.write(data)
        except Exception as e:
            msg = json.dumps({"error": str(e)}).encode()
            self.send_response(502)
            self.send_header("Content-Type", "application/json")
            self._cors()
            self.end_headers()
            self.wfile.write(msg)

if __name__ == "__main__":
    with socketserver.TCPServer(("0.0.0.0", 8080), Handler) as httpd:
        print("Сервер на http://localhost:8080/  (Ctrl+C для остановки)")
        httpd.serve_forever()
