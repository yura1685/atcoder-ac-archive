from more_itertools import run_length
ans = []
for alp, cnt in run_length.encode(input()):
    ans.append(alp)
    ans.append(cnt)
print(*ans)