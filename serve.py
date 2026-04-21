import http.server
import socketserver
import webbrowser
import os

PORT = 3000
os.chdir(os.path.dirname(os.path.abspath(__file__)))

handler = http.server.SimpleHTTPRequestHandler
handler.extensions_map.update({'.html': 'text/html'})

print(f"\n{'='*50}")
print(f"  Portfolio running at: http://localhost:{PORT}")
print(f"  Press Ctrl+C to stop")
print(f"{'='*50}\n")

webbrowser.open(f"http://localhost:{PORT}")

with socketserver.TCPServer(("", PORT), handler) as httpd:
    httpd.serve_forever()
