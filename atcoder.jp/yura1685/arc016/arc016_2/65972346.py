from more_itertools import run_length

N = int(input())

f = []
for _ in range(N):
    f.append(input())

f2 = list(zip(*f))

tap = 0

for i in f2:
    tap += i.count('x')
    L = list(run_length.encode(''.join(i)))
    for j in L:
        if j[0] == 'o':
            tap += 1
print(tap)