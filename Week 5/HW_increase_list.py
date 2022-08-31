# list = list(map(int, input().split()))
# print(' '.join(map(str, list)))
# print(*list)
def IsAscending(a):
    i = 1
    while i < len(a) and a[i] > a[i - 1]:
        i += 1
    return i // len(a)


list = list(map(int, input().split()))
print('YES' * IsAscending(list),
      'NO' * int((IsAscending(list) + 1) % 2), sep='')
