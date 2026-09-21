"""
This file demonstrates Python managed attributes (properties).

What this file means:
- A property lets you access a method like a normal attribute.
- `@property` defines getter logic for reading (`obj.name`).
- `@name.setter` defines setter logic for assignment (`obj.name = value`).
- `@name.deleter` defines deleter logic (`del obj.name`).

Why the underscore name (`_name`) exists:
- `_name` is the internal storage attribute.
- `name` is the public property API that controls access.
"""


class Person:
    def __init__(self):
        # Convention: internal storage for property value uses leading underscore.
        self._name = None

    @property
    def name(self):
        # Getter: called when reading p.name
        # NOTE: this mutates value every read (for demo only).
        self._name= self._name + " is property"
        return self._name

    @name.setter
    def name(self, name):
        # Setter: called when assigning p.name = "..."
        self._name = name+" is setter"

    @name.deleter
    def name(self):
        # Deleter: called when using del p.name
        del self._name

if __name__ == "__main__":
    # Demo flow:
    # 1) set value through setter
    # 2) read value through getter
    # 3) delete value through deleter
    p = Person()
    p.name = "John"
    print(p.name)
    del p.name