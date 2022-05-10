from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url_components = parse.urlsplit(self.path)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        if "word" in dic:
            url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
            full_url = url + dic["word"]
            response = requests.get(full_url)
            data = response.json()

            definitions = []
            for word_data in data:
                definition = word_data["meanings"][0]["definitions"][0]["definition"]
                definitions.append(definition)

            message = str(definitions)

        else:
            message = "Give me a word to define please"

        # common
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()

        self.wfile.write(message.encode())

        #return