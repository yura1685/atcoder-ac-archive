from random import randint

N, Q = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

n = 1 << 60
LA, LB = [0] * (N+1), [0] * (N+1)

d = {}
def get_hash(x):
    if x not in d:
        d[x] = randint(1,n)
    return d[x]

for i in range(N):
    LA[i+1] = LA[i] + get_hash(A[i])

for i in range(N):
    LB[i+1] = LB[i] + get_hash(B[i])

for _ in range(Q):
    l, r, L, R = map(int,input().split())
    X = LA[r] - LA[l-1]
    Y = LB[R] - LB[L-1]
    print('Yes' if X == Y else 'No')