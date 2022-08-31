from math import sqrt

print(
    2,
    *filter(
        lambda x: 0 not in set(
            map(
                lambda y: x % y,
                range(2, int(sqrt(x)) + 1)
            )
        ),
        range(3, int(input()) + 1, 2)
    )
)
