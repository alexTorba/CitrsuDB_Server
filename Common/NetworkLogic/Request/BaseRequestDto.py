from Common.JsonLogic.JsonContract import JsonContract


class BaseRequestDto(JsonContract, object):
    server_method: str

    _json_fields = {
        "s": "server_method",
    }
