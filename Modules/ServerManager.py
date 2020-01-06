from Common.NetworkLogic import TCPHandler


class ServerManager:
    @staticmethod
    def start_server():
        TCPHandler.start_listating()
