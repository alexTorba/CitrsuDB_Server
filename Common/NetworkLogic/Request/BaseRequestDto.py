from Common.JsonLogic.JsonContract import JsonContract


class BaseRequestDto(JsonContract, object):
    server_method: str

    _json_fields = {
        "s": "server_method",
    }

    def __init__(self, server_method: str) -> None:
        if server_method is not None:
            self.server_method = server_method
