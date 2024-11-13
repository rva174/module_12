#11.3 ДЗ по теме "Интроспекция"

class Info:
    Info = {}
    def __init__(self, obj):
        self.obj = obj

def introspection_info(self):
    info = {
        'type': type(obj).__name__,
        'attributes': dir(obj),
        'methods': [method for method in dir(obj) if callable(getattr(obj, method))],
        'doc_string': obj.__doc__,
        'is_instance': isinstance(obj, object)
    }

    return info

obj = [3, 'abc', 8]
result = introspection_info(obj)

for key, value in result.items():
    print(f"{key}: {value}")