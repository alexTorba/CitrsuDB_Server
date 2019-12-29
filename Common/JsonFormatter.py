import inspect
from json import dumps
from json import loads

from Common.JsonContract import JsonContract


class JsonFormatter:

    @staticmethod
    def __object_to_dict(obj):
        if obj is None or not isinstance(obj, JsonContract):
            raise Exception("the object must implement JsonContract !")

        fields = dict()
        fields.update(obj.to_minimize_dict())

        for k, v in fields.items():
            if isinstance(v, JsonContract):
                fields[k] = JsonFormatter.__object_to_dict(v)
            elif hasattr(v, "__getitem__") and not isinstance(v, str):
                for index, item in enumerate(v):
                    if isinstance(item, JsonContract):
                        v[index] = JsonFormatter.__object_to_dict(item)

        return fields

    @staticmethod
    def dumps(obj: JsonContract) -> str:
        obj_dict_view = JsonFormatter.__object_to_dict(obj)
        return dumps(obj_dict_view, ensure_ascii=False)

    @staticmethod
    def __json_to_instance(obj, cls: type):
        instance: cls = cls()
        annotations: dict = cls.__annotations__

        for name, value in obj.items():
            full_field_name = instance.json_to_field(name)
            type_value = annotations.get(full_field_name)
            if hasattr(type_value, "__args__"):  # if type is Generic List with users type
                items_type = type_value.__args__[0]
                if inspect.isclass(items_type) and issubclass(items_type, JsonContract):
                    for index, item in enumerate(value):
                        item = JsonFormatter.__json_to_instance(item, items_type)
                        value[index] = item
            elif issubclass(type_value, JsonContract):
                value = JsonFormatter.__json_to_instance(value, type_value)
            setattr(instance, full_field_name, value)
        return instance

    @staticmethod
    def loads(data: str, cls):
        obj = loads(data)
        return JsonFormatter.__json_to_instance(obj, cls)
