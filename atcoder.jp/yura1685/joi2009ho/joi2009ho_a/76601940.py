from more_itertools import run_length
N = int(input())
M = int(input())
ans = 0
for alp, cnt in run_length.encode(input().replace('IO', 'X').replace('XI', 'XXO').replace('I', 'O')):
    if alp == 'O':
        continue
    ans += max(cnt - N, 0)
print(ans)