n = int(input())

students = [input().split() for _ in range(n)]
students.sort(key=lambda man: -int(man[1]))

[print(man[0]) for man in students]
