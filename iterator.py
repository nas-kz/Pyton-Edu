"""
Demonstrates iterator protocol with `__iter__` and `__next__`.

What this file shows:
- Iteration state is stored in `self.value`.
- The class can be used directly in a `for` loop.
"""

class IterClass:
    def __init__(self):
        self.value = 0

    def __iter__(self):
        # For this simple example, the object is its own iterator.
        return self

    def __next__(self):
        if self.value < 10:
            x = self.value
            self.value += 1
            return x
        else:
            # Required to stop the `for` loop.
            raise StopIteration
        

if __name__ == "__main__":
    for i in IterClass():
        print(i)