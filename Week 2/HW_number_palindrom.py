k = int(input())
dig = 0
i = 0
rev = ''
n = 1
m = 0

while m < k:
    while n != 0:
        dig = n % 10
        rev = str(rev) + str(dig)
        n //= 10
    if (int(rev)) == m + 1:
        i += 1
    rev = ''
    m += 1
    n = m + 1

print(i)
