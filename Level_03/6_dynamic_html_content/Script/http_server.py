from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler


class MyServer(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Sending an '200 OK' response
        self.send_response(200)
        self.end_headers()
        # self.send_header("Content-type", "text/html")
        # self.end_headers()
        # content = f"<h1>Hello!, The Current Time is, {datetime.now()}</h1>"
        # self.wfile.write(content.encode())
        # # Setting the header
        # self.send_header("Content-type", "text/html")

        # # Whenever using 'send_header', you also have to call 'end_headers'

        # # Some custom HTML code, possibly generated by another function
        # html = "<html><head></head><body><h1>Hello World!</h1></body></html>"
        # print(html, html.encode("utf-8"))
        # # Writing the HTML contents with UTF-8
        # self.wfile.write(html.encode())
        return


addr = "127.0.0.1"
port = 8080
server_address = (addr, port)
httpd = HTTPServer(server_address, MyServer)

print(f"Starting httpd server on {addr}:{port}")
httpd.serve_forever()