from http.server import BaseHTTPRequestHandler
from urllib import parse


class handler(BaseHTTPRequestHandler):
    def do_GET(self):

        path = self.path
        url_components = parse.urlsplit(path)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        name = dic.get("name")

        if name:
            message = f"Aloha {name}"
        else:
            message = "Aloha stranger"

        self.wfile.write(message.encode())
        return