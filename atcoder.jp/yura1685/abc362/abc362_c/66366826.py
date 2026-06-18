N = int(input())

m, M = 0, 0
pair = [tuple(map(int,input().split())) for _ in range(N)]
for L, R in pair:
    m += L
    M += R

if not m <= 0 <= M:
    print('No')
    exit()

print('Yes')

want = -m

for L, R in pair:
    n = R - L
    if want == 0:
        print(L, end=' ')
    elif want > n:
        print(R, end=' ')
        want -= n
    else:
        print(L+want, end=' ')
        want = 0
    