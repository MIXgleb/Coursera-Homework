from sys import stdin
from functools import reduce

print(
    reduce(
        lambda x, y: x * y,
        map(
            lambda x: x**5,
            map(
                int,
                stdin.readline().split()
            )
        )
    )
)
