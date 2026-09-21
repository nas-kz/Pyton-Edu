"""
Demonstrates a lambda-based sum idea.

What this file means:
- `lambda` creates a small anonymous function.
- This snippet intends to accumulate values in a range.
"""

sumx = lambda x, n: sum(range(n))

print(sumx(0, 10))