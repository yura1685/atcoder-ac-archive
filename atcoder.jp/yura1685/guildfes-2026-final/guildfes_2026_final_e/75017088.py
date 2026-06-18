N, Q = map(int, input().split())
S = list(input())
i = 0
for _ in range(Q):
    q, x = map(int, input().split())
    x -= 1
    if q == 1:
        S[x+i], S[x+i+1] = S[x+i+1], S[x+i]
    else:
        i += x + 1

print(''.join(S[i:]))