I = input().split()
N, Q = int(I[0]), int(I[1])
A = list(map(int, input().split()))
B = int(N / Q ** 0.5)
if B < 1: B = 1
query = []
for i in range(Q):
    I = input().split()
    l, r = int(I[0]) - 1, int(I[1]) - 1
    query.append((l//B, r, l, i))
query.sort()

anss = [0] * Q
cnt = [0] * (max(A) + 1)

def f(x): return x*(x-1)*(x-2) // 6

ans = 0
lastl, lastr = 0, -1
for block, r, l, i in query:
    while lastr < r:
        lastr += 1
        x = A[lastr]
        cnt[x] += 1
        ans += f(cnt[x]) - f(cnt[x]-1)

    while lastl > l:
        lastl -= 1
        x = A[lastl]
        cnt[x] += 1
        ans += f(cnt[x]) - f(cnt[x]-1)

    while lastr > r:
        x = A[lastr]
        cnt[x] -= 1
        lastr -= 1
        ans += - f(cnt[x]+1) + f(cnt[x])

    while lastl < l:
        x = A[lastl]
        cnt[x] -= 1
        lastl += 1
        ans += - f(cnt[x]+1) + f(cnt[x])

    anss[i] = ans

for a in anss:
    print(a)