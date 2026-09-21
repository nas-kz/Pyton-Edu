"""
Demonstrates a custom iterator class.

What this file shows:
- The object is its own iterator via `__iter__`.
- `__next__` returns values until `StopIteration`.
"""

class CustomGenerator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        # Return iterator object (self).
        return self

    def __next__(self):
        if self.start < self.end:
            value = self.start
            self.start += 1
            return value
        else:
            # Signal that iteration is finished.
            raise StopIteration
        

for x in CustomGenerator(1, 10):
    print(x)

