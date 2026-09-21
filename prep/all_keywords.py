import builtins
from pathlib import Path
import logging

OUTPUT_FILE = Path(__file__).with_name("example.txt")
OUTPUT_FILE.write_text("", encoding="utf-8")


def print(*args, **kwargs):
    builtins.print(*args, **kwargs)
    file_kwargs = {}
    if "sep" in kwargs:
        file_kwargs["sep"] = kwargs["sep"]
    if "end" in kwargs:
        file_kwargs["end"] = kwargs["end"]
    with OUTPUT_FILE.open("a", encoding="utf-8") as output:
        builtins.print(*args, **file_kwargs, file=output)


int_var = 10
float_var = 3.14
complex_var = 2+3j
str_var = "hello world"
bool_var = True
list_var = [1,2,3]
tuple_var = (1,2,3)
set_var = {1,2,3}
dict_var = {"name": "John", "age": 30}
none_var = None

print(int_var)
print(float_var)
print(complex_var)
print(str_var)
print(bool_var)
print(list_var)
print(tuple_var)
print(set_var)
print(dict_var)

# conditional statements
if int_var > 10:
    print("int_var is positive")
elif int_var < 0:
    print("int_var is negative")
else:
    print("int_var is zero")

switch_var = "apple1"
match switch_var:
    case "apple":
        print("apple")
    case _:
        print("unknown")

# loops
for i in range(10):
    if i % 2 == 0:
        print(f"i is even: {i}")
    else:
        print(f"i is odd: {i}")

else:
    print("for loop is finished")

while int_var < 10:
    print(int_var)
    int_var += 1

else:
    print("while loop is finished")

# break and continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(f"i is odd: {i}")
    
int_var = 10
# infinite loop
while True:
    # enter prompt
    prompt = input("Enter a command: ")
    print(f"You entered: {prompt}")
    prompt = "exit"
    if prompt == "exit":
        break
    else:
        print(f"You entered: {prompt}")

# try except finally
try:
    print(int_var / 0)
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Finally block")

# raise statement
#raise Exception("This is an exception")

# assert statement
# assert int_var > 10, "int_var is not greater than 10"
# with statement
logging.basicConfig(level=logging.INFO)
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

# logging statement
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("This is an error message")
logging.critical("This is a critical message")

def add(a, b):
    return a+b

# loop statement
for i in range(10):
    print(f"i is {i}")
    print("add(i, i) is", add(i, i))
    for j in range(10):
        print(f"j is {j}")
        print("for for loop add(j, j) is", add(j, j))
    print("for loop is finished")


# lambda function
lambda_func = lambda x: x + 1
print("lambda_func(1) is", lambda_func(1))

# list comprehension
list_comp = [i for i in range(10)]
print("list_comp is", list_comp)

# dictionary comprehension
dict_comp = {i: i for i in range(10)}
print("dict_comp is", dict_comp)

# set comprehension
set_comp = {i for i in range(10)}
print("set_comp is", set_comp)

# tuple comprehension
tuple_comp = (i for i in range(10))
print("tuple_comp is", tuple_comp)

# generator expression
generator_expr = (i for i in range(10))
print("generator_expr is", generator_expr)

# generator function
def generator_func():
    for i in range(10):
        yield i

print("generator_func is", generator_func()) 

# class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self, prompt):
        print(f"{prompt} {self.name} is {self.age} years old")

person = Person("John", 30)
person.say("Hello")

# inheritance
class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

student = Student("John", 30, "A")
student.say("Hello")

# polymorphism
class Animal:
    def __init__(self, name):
        self.name = name

    def say(self, prompt):
        print(f"{prompt} {self.name} is an animal")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

dog = Dog("Rex", "Labrador")
dog.say("Hello")

# interface
class AnimalInterface:
    def say(self, prompt):
        pass

class Dog(AnimalInterface):
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def say(self, prompt):
        print(f"{prompt} {self.name} is a dog of breed {self.breed}")

dog = Dog("Rex", "Labrador")
dog.say("Hello")

# Abstract class
class AnimalAbstract:
    def __init__(self, name):
        self.name = name

    def say(self, prompt):
        pass

class Dog(AnimalAbstract):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed