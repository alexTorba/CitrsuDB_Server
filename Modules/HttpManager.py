from collections import Callable
from http.server import HTTPServer, BaseHTTPRequestHandler
from typing import Dict
import socketserver
from Modules.GroupManager import GroupManager
from Modules.StudentManager import StudentManager


class HttpManager(BaseHTTPRequestHandler):
    __handler: dict  # key - url, value - handler
    __managers: list = [StudentManager, GroupManager]

    def init_managers(self):
        for m in self.__managers:
            m.init(self.__handler)

    def do_POST(self):
        context_length = int(self.headers["Content-Length"])
        body = self.rfile.read(context_length)
        print(body)
        print()

    @staticmethod
    def start_server():
        httpd = HTTPServer(("127.0.0.1", 8000), HttpManager)
        httpd.serve_forever()
