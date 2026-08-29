import http.server, socketserver, webbrowser, os, threading, time, glob

PORT = 8765
HTML = "editor_v4.3.html"
if not os.path.exists(HTML):
    htmls = glob.glob("*.html")
    if htmls: HTML = htmls[0]

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def open_browser():
    time.sleep(1)
    webbrowser.open(f"http://localhost:{PORT}/{HTML}")

threading.Thread(target=open_browser, daemon=True).start()

with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
    print(f"Server: http://localhost:{PORT}/{HTML}")
    print("Press Ctrl+C to stop")
    httpd.serve_forever()
