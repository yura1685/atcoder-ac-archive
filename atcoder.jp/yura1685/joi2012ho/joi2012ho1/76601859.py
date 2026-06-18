from more_itertools import run_length

S = list(run_length.encode(input()))
N = len(S)
ans = 0
for i, (alp, co) in enumerate(S):
    if alp != 'O':
        continue
    if i == 0 or i == N - 1:
        continue
    if S[i-1][0] != 'J' or S[i+1][0] != 'I':
        continue
    cj, ci = S[i-1][1], S[i+1][1]
    if cj >= co and ci >= co:
        ans = max(ans, min(cj, co, ci))

print(ans)