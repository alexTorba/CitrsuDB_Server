import inspect
from typing import TypeVar, get_origin, Dict


class TypeInspect:
    __cache: Dict[type, dict] = dict()

    @classmethod
    def get_annotations(cls, inspected_type: type) -> dict:
        if inspected_type in TypeInspect.__cache:
            return TypeInspect.__cache[inspected_type]

        full__ann = TypeInspect.__get_full_annotations(inspected_type)
        TypeInspect.__set_generic_type(inspected_type, full__ann)

        TypeInspect.__cache[inspected_type] = full__ann
        return full__ann

    @staticmethod
    def __get_full_annotations(cls: type) -> dict:
        origin = get_origin(cls)  # get class instead of _GenericAlias
        if origin is not None:
            cls = origin
        if not hasattr(cls, "__annotations__"):
            return dict()
        annotation: dict = cls.__annotations__
        if hasattr(cls, "__bases__"):
            bases = cls.__bases__
            for b in bases:
                annotation.update(TypeInspect.__get_full_annotations(b))
        return annotation

    @staticmethod
    def __set_generic_type(cls: type, annotations: dict) -> None:
        for n, v in annotations.items():
            if type(v) is TypeVar:
                annotations[n] = TypeInspect.__get_generic_type(cls)

    @staticmethod
    def __get_generic_type(cls: type) -> type:
        if get_origin(cls) is not None:
            return cls.__dict__.get("__args__")[0]
        return inspect.getattr_static(cls, "__orig_bases__")[0].__dict__.get("__args__")[0]
