from more_itertools import run_length

def solve(s: str):
    c = list(run_length.encode(s))
    n = len(c)
    a, b = 0, 0
    if n <= 2:
        return 0
    A0, B1 = [], []
    for i in range(n):
        if c[i][0] == '1':
            A0.append(c[i][1])
            B1.append(0)
        else:
            B1.append(c[i][1])
            A0.append(0)
    dif = [B1[i] - A0[i] for i in range(n)]
    ans = 10**10
    now = 0
    for d in dif:
        now = min(d, now+d)
        ans = min(ans, now)
    return sum(A0) + ans

T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    print(solve(S))