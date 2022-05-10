from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        url_components = parse.urlsplit(self.path)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        if "name" in dic:
            url = "https://restcountries.com/v3.1/name/"
            query = dic["name"]

            response = requests.get(url + dic["name"])
            data = response.json()

            cap = data[0]["capital"][0]
            cap_str = str(cap)
            message = f"The capital of {query} is {cap_str}."

            self.wfile.write(message.encode())

        return
