"""
Demonstrates `__slots__` in Python classes.

What this file shows:
- `__slots__` limits which attributes instances can have.
- This can reduce memory usage and prevent accidental new attributes.
"""

class MyClass:
    __slots__ = ('name', 'age', 'city') # Ограничиваем набор атрибутов

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

# Теперь объекты класса MyClass могут иметь только атрибуты name, age, city
obj = MyClass("Иван", 30, "Шымкент")
print(obj.name) # "Иван"

# Попытка добавить новый атрибут вызовет ошибку:
# obj.job = "Программист" # AttributeError: 'MyClass' object has no attribute 'job'