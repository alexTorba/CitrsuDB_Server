import inspect
from typing import TypeVar, get_origin


class TypeInspect:
    @staticmethod
    def get_annotations(cls: type) -> dict:
        full__ann = TypeInspect.__get_full_annotations(cls)
        TypeInspect.__set_generic_type(cls, full__ann)
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
        base_classes = [attr for attr in inspect.classify_class_attrs(cls) if attr.name == '__orig_bases__'][0].object
        generic = [c for c in base_classes if get_origin(c) is not None][0]
        return generic.__dict__.get("__args__")[0]
