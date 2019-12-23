from json import dumps
from json import loads
from typing import List

from Common.IJsonFormatable import IJsonFormatable


class JsonFormatter:

    @staticmethod
    def __object_to_dict(obj):
        if not isinstance(obj, IJsonFormatable):
            raise Exception("the object must implement IJsonFormattable !")

        fields = dict()
        fields.update(obj.to_json())

        for k, v in fields.items():
            if hasattr(v, "__getitem__") and not isinstance(v, str):
                for index, item in enumerate(v):
                    v[index] = JsonFormatter.__object_to_dict(item)
            else:
                if isinstance(v, IJsonFormatable):
                    v = JsonFormatter.__object_to_dict(v)
                    fields[k] = v

        return fields

    @staticmethod
    def dumps(obj: IJsonFormatable) -> str:
        obj_dict_view = JsonFormatter.__object_to_dict(obj)
        return dumps(obj_dict_view, ensure_ascii=False)

    @staticmethod
    def __json_to_instance(obj, cls: type):
        annotations: dict = cls.__annotations__ if hasattr(cls, "__annotations__") else None
        if issubclass(cls, List):
            instance: List[cls] = list()
            for item in obj:
                item = JsonFormatter.__json_to_instance(item, type(item))
                instance.append(item)
        else:
            instance: cls = cls()
            # todo:a из минимизированного значения получить полное имя поля ("p"=>"person")
            for name, value in obj.items():
                if hasattr(instance, "json_to_field"):
                    full_field_name = instance.json_to_field(min_field=name)
                    type_instance = annotations.get(full_field_name)
                    value = JsonFormatter.__json_to_instance(value, type_instance)
                setattr(instance, name, value)
            return instance

    @staticmethod
    def loads(data: str, cls):
        obj = loads(data)
        return JsonFormatter.__json_to_instance(obj, cls)
