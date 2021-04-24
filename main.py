#!/usr/bin/env python3
import json
import urllib.parse
import logging
from countStars import count_stars_for_user
from http.server import HTTPServer, BaseHTTPRequestHandler


class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()

    def do_GET(self):
        if self.path.find("?") != -1:
            parsed = urllib.parse.urlparse(self.path)
            url_list = urllib.parse.parse_qs(parsed.query)
            if "username" in url_list:
                owner = url_list["username"][0]
        else:
            owner = self.path[1:].split("/")[0]
        try:
            repos, num_of_stars = count_stars_for_user(owner)
            show = {"repositories": repos, "num_of_stars": num_of_stars}
            self.wfile.write(json.dumps(show, indent=1).encode("utf-8"))
        except Exception as e:
            print(e)


def run(server_class=HTTPServer, handler_class=S, port=8000):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting server \n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
        logging.info('Stopping server\n')


if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
