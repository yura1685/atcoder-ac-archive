from random import randint

N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

n = 1 << 60
SA, SB = [0] * (N+1), [0] * (N+1)

d = {}
def get_hash(x):
    if x not in d:
        d[x] = randint(1,n)
    return d[x]

s = set()
for i in range(N):
    a = A[i]
    hash = 0
    if a in s: pass
    else:
        s.add(a)
        hash = get_hash(a)
    SA[i+1] = SA[i] + hash

s.clear()
for i in range(N):
    b = B[i]
    hash = 0
    if b in s: pass
    else:
        s.add(b)
        hash = get_hash(b)
    SB[i+1] = SB[i] + hash

Q = int(input())
for _ in range(Q):
    x, y = map(int,input().split())
    print('Yes' if SA[x] == SB[y] else 'No')