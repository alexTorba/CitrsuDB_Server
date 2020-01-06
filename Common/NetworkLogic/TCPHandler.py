import socketserver
from typing import Dict, cast
from Common.NetworkLogic.BaseRequestDto import BaseRequestDto
from Common.JsonLogic.JsonFormatter import JsonFormatter


class Test(JsonContract):
    age: int
    name: str
    _json_fields = {
        "a": "age",
        "n": "name"
    }

    def __init__(self, age=None, name=None):
        if age is not None:
            self.age = age
        if name is not None:
            self.name = name


class TCPHandler(socketserver.ThreadingMixIn, socketserver.BaseRequestHandler):
    __method_type: Dict[str, type] = {"test", Test}

    def handle(self):
        data = self.request.recv(2048).strip().decode()
        base_dto = cast(JsonFormatter.deserialize(data, BaseRequestDto), BaseRequestDto)
        print(base_dto.server_method)

    @staticmethod
    def start_listating():
        with socketserver.TCPServer(("127.0.0.1", 8888), TCPHandler) as sock:
            print("Start listening")
            sock.serve_forever()
