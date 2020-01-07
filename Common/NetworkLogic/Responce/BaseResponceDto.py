from Common.JsonLogic.JsonContract import JsonContract


class BaseResponceDto(JsonContract):
    status_code: int

    @property
    def _json_fields(self) -> dict:
        return {
            "s": "status_code"
        }

    def __init__(self, status_code: int) -> None:
        if status_code is not None:
            self.status_code = status_code
