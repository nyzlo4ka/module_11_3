from pprint import pprint


def introspection_info(obj):
    obj_type = type(obj)
    all_attrs = dir(obj)
    attributes = [attr for attr in all_attrs if not callable(getattr(obj, attr))]
    methods = [attr for attr in all_attrs if callable(getattr(obj, attr))]
    obj_module = getattr(obj, "__module__", "Неизвестно")
    doc = getattr(obj, "__doc__", "Нет документации")
    class_name = getattr(obj, "__class__", obj_type).__name__
    return {
        "type": obj_type.__name__,
        "class_name": class_name,
        "attributes": attributes,
        "methods": methods,
        "module": obj_module,
        "doc": doc
    }


class MyClass:
    def __init__(self, value):
        self.value = value

    def my_method(self):
        return self.value


my_object = MyClass(42)
number_info = introspection_info(my_object)
pprint(number_info)
