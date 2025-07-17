import http.server
import socketserver
import os

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Get the file system path
        fs_path = self.translate_path(self.path)

        # If the path doesn't exist, try adding .html
        if not os.path.exists(fs_path):
            # Check if adding .html makes it a valid file
            if os.path.exists(fs_path + '.html'):
                self.path += '.html'

        return http.server.SimpleHTTPRequestHandler.do_GET(self)


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever() 