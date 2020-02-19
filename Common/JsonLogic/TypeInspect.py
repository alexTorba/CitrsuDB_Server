import inspect
from typing import TypeVar, get_origin, Dict, Union


class TypeInspect:
    __cache_annotations: Dict[type, dict] = dict()
    __cache_generic_type: Dict[type, type] = dict()

    @classmethod
    def get_annotations(cls, inspected_type: type) -> dict:
        if inspected_type in TypeInspect.__cache_annotations:
            return TypeInspect.__cache_annotations[inspected_type]

        full__ann = TypeInspect.__get_full_annotations(inspected_type)
        TypeInspect.__set_generic_type(inspected_type, full__ann)

        TypeInspect.__cache_annotations[inspected_type] = full__ann
        return full__ann

    @staticmethod
    def __get_full_annotations(cls: type) -> Union[dict, None]:
        origin = get_origin(cls)  # get class instead of _GenericAlias
        if origin is not None:
            cls = origin
        if not hasattr(cls, "__annotations__"):
            return None
        annotation: dict = cls.__annotations__
        if hasattr(cls, "__bases__"):
            bases = cls.__bases__
            for b in bases:
                b_ann = TypeInspect.__get_full_annotations(b)
                if b_ann is not None:
                    annotation.update(b_ann)
        return annotation

    @staticmethod
    def __set_generic_type(cls: type, annotations: dict) -> None:
        for n, v in annotations.items():
            if type(v) is TypeVar:
                annotations[n] = TypeInspect.__get_generic_type(cls)

    @classmethod
    def __get_generic_type(cls, cls_type: type) -> type:
        if get_origin(cls_type) is not None:
            return cls_type.__dict__.get("__args__")[0]

        if cls_type in cls.__cache_generic_type:
            return cls.__cache_generic_type[cls_type]

        generic_type = inspect.getattr_static(cls_type, "__orig_bases__")[0].__dict__.get("__args__")[0]
        cls.__cache_generic_type[cls_type] = generic_type
        return generic_type
