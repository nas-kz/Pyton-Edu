"""
Demonstrates `yield` and a simple generator function.

What this file shows:
- A normal `for` loop over a list.
- A generator that yields values one-by-one lazily.
"""

# example yield
arr = ['Alice', 'Bob', 'Charlie']
def my_generator(arr):
    # `yield` returns one value at a time and pauses function state.
    for name in arr:
        yield name
if __name__ == '__main__':
    print("For List")
    for name in arr:
        print(name)
    print("Generator")
    for name in my_generator(arr):
        print(name)
        