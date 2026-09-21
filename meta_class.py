"""
Demonstrates a basic custom metaclass.

What this file shows:
- `MetaClass.__new__` injects attributes during class creation.
- Classes using this metaclass receive injected members automatically.
"""

class MetaClass(type):
    def __new__(cls, name, bases, attrs):
        # Add class attribute at class-definition time.
        attrs['name'] = 'MetaClass'
        return type.__new__(cls, name, bases, attrs)
    

class MyClass(metaclass=MetaClass):
    pass


mc = MyClass()
print(mc.name)