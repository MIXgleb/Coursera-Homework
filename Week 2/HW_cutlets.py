k = int(input())
m = int(input())
n = int(input())

time1 = ((n + k - 1) // k) * 2 * m
time2 = 0

if k % 2 == 0:
    if n % (3 * k // 2) == 0:
        time2 = n // (3 * k // 2) * 3 * m
        # print(number // (3 * k // 2) * 3 * m)
    elif n % (3 * k // 2) <= k:
        time2 = n // (3 * k // 2) * 3 * m + 2 * m
        # print(number // (3 * k // 2) * 3 * m + 2 * m)
    elif k < n % (3 * k // 2) <= (3 * k) // 2:
        time2 = n // (3 * k // 2) * 3 * m + 3 * m
        # print(number // (3 * k // 2) * 3 * m + 3 * m)

if k % 2 == 1:
    if n % (3 * k) == 0:
        time2 = n // (3 * k) * 6 * m
        # print(number // (3 * k) * 6 * m)
    elif n % (3 * k) <= k:
        time2 = n // (3 * k) * 6 * m + 2 * m
        # print(number // (3 * k) * 6 * m + 2 * m)
    elif k < n % (3 * k) <= (3 * k - 1) // 2:
        time2 = n // (3 * k) * 6 * m + 3 * m
        # print(number // (3 * k) * 6 * m + 3 * m)
    elif (3 * k - 1) // 2 < n % (3 * k) <= 2 * k:
        time2 = n // (3 * k) * 6 * m + 4 * m
        # print(number // (3 * k) * 6 * m + 4 * m)
    # elif 2 * k < number % (3 * k) <= (k + k // 2 + 1 + (k - 1) // 2):
    #     time2 = number // (3 * k) * 6 * m + 5 * m
    #     # print(number // (3 * k) * 6 * m + 5 * m)
    elif 2 * k < n % (3 * k) <= 3 * k:
        time2 = n // (3 * k) * 6 * m + 6 * m
        # print(number // (3 * k) * 6 * m + 6 * m)

print(min(time1, time2))
