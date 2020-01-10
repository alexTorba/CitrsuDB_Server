import socketserver

from Common.JsonLogic.JsonFormatter import JsonFormatter
from Common.NetworkLogic.Request.BaseRequestDto import BaseRequestDto
from Modules.StudentManager import StudentManager


class TCPHandler(socketserver.ThreadingMixIn, socketserver.BaseRequestHandler):
    # key - command_name, value - tuple(dto_type, handler)
    __method_handler: dict
    __managers: list = [StudentManager]

    def __init__(self, request, client_address, server):
        super().__init__(request, client_address, server)
        for m in self.__managers:
            m.init(self.__method_handler)

    def handle(self):
        data, socket = self.request
        data = data.decode("utf-8")

        base_dto = JsonFormatter.deserialize(data, BaseRequestDto)
        (dto_type, handler) = self.__method_handler.get(base_dto.server_method)
        dto = JsonFormatter.deserialize(data, dto_type)

        responce_dto = handler(dto)
        j_son = JsonFormatter.serialize(responce_dto)
        responce_data = bytes(j_son, "utf-8")
        socket.send(responce_data)

    @staticmethod
    def start_listening():
        with socketserver.TCPServer(("127.0.0.1", 8888), TCPHandler) as sock:
            print("Start listening")
            sock.serve_forever()
