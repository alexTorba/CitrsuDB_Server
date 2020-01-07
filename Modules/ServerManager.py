from Common.NetworkLogic.TCPHandler import TCPHandler


class ServerManager:
    @staticmethod
    def start_server():
        TCPHandler.start_listening()
