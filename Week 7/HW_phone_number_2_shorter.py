n_l = []

for _ in range(4):
    n_l.append(''.join([i for i in input() if i.isdigit()]))
    n_l[_] = '8495' + n_l[_] if len(n_l[_]) == 7 else n_l[_]

[print(['NO', 'YES'][n_l[0][1:] == n_l[i][1:]]) for i in range(1, 4)]
