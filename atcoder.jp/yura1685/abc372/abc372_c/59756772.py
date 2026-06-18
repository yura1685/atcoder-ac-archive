def check(x):
    abc = 0
    for i in range(len(x)-2):
        if x[i:i+3] == ['A','B','C']:
            abc += 1
    return abc

N, Q = map(int,input().split())
S = list(input())
ans = 0

for i in range(N-2):
    if S[i:i+3] == ['A','B','C']:
        ans += 1

for i in range(Q):
    n, s = map(str,input().split())
    n = int(n)
    if n == 1:
        p = [s] + S[1:3]
        ans = ans - check(S[:3]) + check(p)
        S[0] = s
        print(ans)
    elif n == 2:
        p = [S[0]] + [s] + S[2:4]
        ans = ans - check(S[:4]) + check(p)
        S[1] = s
        print(ans)
    elif n == N:
        p = S[-3:-1] + [s]
        ans = ans - check(S[-3:]) + check(p)
        S[-1] = s
        print(ans)
    elif n == N - 1:
        p = S[-4:-2] + [s] + [S[-1]]
        ans = ans - check(S[-4:]) + check(p)
        S[-2] = s
        print(ans)
    else:
        p = S[n-3:n-1] + [s] + S[n:n+2]
        ans = ans - check(S[n-3:n+2]) + check(p)
        S[n-1] = s
        print(ans)