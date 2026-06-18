from more_itertools import run_length

s = input()
L = list(run_length.encode(s))

ans = ''
for i in L:
    ans += i[0] + str(i[1])

print(ans)