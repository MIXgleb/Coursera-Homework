# list = list(map(int, input().split()))
# print(' '.join(map(str, list)))
# print(*list)


def reverse(a):
    return a[::-1]


print(*reverse(input().split()))
