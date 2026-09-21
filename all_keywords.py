"""
===========================
  PYTHON BUILT-IN EXAMPLES
===========================

This file includes:
1. General variables and types
2. Built-in functions with examples
3. Common keywords (explained in comments)
"""

# =========================================
# 1️⃣ GENERAL VARIABLES & BASIC DATA TYPES
# =========================================

# Numbers
x_int = 10            # Integer
x_float = 3.14        # Floating-point
x_complex = 2 + 3j    # Complex number

# Strings
text = "Hello Python"

# Boolean
is_active = True

# Lists, Tuples, Sets, Dicts
numbers = [1, 2, 3, 4, 5]
coordinates = (10, 20)
unique_items = {1, 2, 3}
person = {"name": "Alice", "age": 25}

# NoneType
nothing = None


# =========================================
# 2️⃣ BUILT-IN FUNCTIONS
# =========================================

# ---- Print & Input ----
print("=== Print and Input ===")
print("Hello, world!")  # Outputs text to console
# name = input("Enter your name: ")  # Uncomment to test
# print("Hi,", name)

# ---- Type Conversion ----
print("\n=== Type Conversion ===")
print(int("10"))       # 10
print(float("3.14"))   # 3.14
print(str(99))         # '99'
print(list("abc"))     # ['a', 'b', 'c']
print(tuple([1, 2]))   # (1, 2)
print(set([1, 2, 2]))  # {1, 2}
print(dict(name="Alice", age=30))  # {'name': 'Alice', 'age': 30}

# ---- Math & Numbers ----
print("\n=== Numeric Functions ===")
print(abs(-7))            # 7 → absolute value
print(round(3.14159, 2))  # 3.14 → round to 2 decimals
print(pow(2, 3))          # 8 → power
print(divmod(10, 3))      # (3, 1) → quotient and remainder

# ---- Sequence Operations ----
print("\n=== Sequence & Iterables ===")
print(len(numbers))       # 5 → length
print(max(numbers))       # 5 → largest element
print(min(numbers))       # 1 → smallest element
print(sum(numbers))       # 15 → sum of elements
print(sorted([3, 1, 2]))  # [1, 2, 3] → sorted copy

# ---- all() & any() ----
print("\n=== all() and any() ===")
print(any([0, 1, 0]))  # True → at least one True
print(all([1, 2, 3]))  # True → all True

# ---- map(), filter(), zip() ----
print("\n=== map(), filter(), zip() ===")
nums = [1, 2, 3]
squares = list(map(lambda x: x ** 2, nums))
print(squares)  # [1, 4, 9]

even = list(filter(lambda x: x % 2 == 0, nums))
print(even)  # [2]

names = ["Alice", "Bob"]
scores = [85, 92]
print(list(zip(names, scores)))  # [('Alice', 85), ('Bob', 92)]

# ---- enumerate() ----
print("\n=== enumerate() ===")
for index, value in enumerate(["a", "b", "c"], start=1):
    print(index, value)

# ---- reversed() ----
print("\n=== reversed() ===")
print(list(reversed([1, 2, 3])))  # [3, 2, 1]

# ---- dir(), type(), isinstance(), id() ----
print("\n=== Object Info Functions ===")
print(type(text))                  # <class 'str'>
print(isinstance(x_int, int))      # True
print(dir([]))                     # All list methods
print(id(x_int))                   # Unique memory ID

# ---- hasattr(), getattr(), setattr(), delattr() ----
print("\n=== Object Attribute Functions ===")
class Person:
    def __init__(self):
        self.name = "Alice"

p = Person()
print(hasattr(p, "name"))   # True
print(getattr(p, "name"))   # Alice
setattr(p, "age", 25)
print(p.age)                # 25
delattr(p, "name")
print(hasattr(p, "name"))   # False

# ---- eval() and exec() ----
print("\n=== eval() and exec() ===")
expression = "2 + 3 * 4"
print(eval(expression))  # 14 → evaluates as Python expression

exec("x = 10; print('x from exec =', x)")  # runs code dynamically

# ---- open() ----
print("\n=== open() for file operations ===")
# Creates a file and writes text (temporary example)
with open("example.txt", "w") as f:
    f.write("Hello File")

# ---- range() ----
print("\n=== range() ===")
for i in range(3):
    print(i)  # 0, 1, 2

# ---- iter() and next() ----
print("\n=== iter() and next() ===")
iterator = iter([10, 20, 30])
print(next(iterator))  # 10
print(next(iterator))  # 20

# ---- del keyword ----
print("\n=== del keyword ===")
temp = [1, 2, 3]
del temp[0]
print(temp)  # [2, 3]

# ---- in keyword ----
print("\n=== in keyword ===")
print(3 in [1, 2, 3])  # True

# ---- help() ----
print("\n=== help() (shows documentation) ===")
# help(str)  # Uncomment to view docs


# =========================================
# 3️⃣ PYTHON KEYWORDS (EXPLAINED IN COMMENTS)
# =========================================
"""
and, or, not      → logical operators
if, elif, else    → conditional branching
for, while, break, continue → loops
def, return       → define and return from functions
class, self       → object-oriented programming
try, except, finally → error handling
with, as          → context management
import, from      → module import
global, nonlocal  → variable scope control
True, False, None → special constants
pass              → empty statement placeholder
yield, lambda     → advanced function constructs
assert            → debugging check
"""

print("\n✅ All examples executed successfully!")
for i in [1, 2, 3]:
    for j in [4, 5, 6]:
        if i > j:
            print(i, j)
        else:
            print(j, i)
print("Generator")
def my_generator():
    for i in [1, 2, 3]:
        yield i

for i in my_generator():
    print(i)