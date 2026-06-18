from collections import deque

Q = int(input())
d = deque([1])
N = 1
M = 1
mod = 998244353
for _ in range(Q):
    q = input().split()
    if q[0] == '1':
        d.append(int(q[1]))
        N += 1
        M = (10*M+int(q[1])) % mod
    if q[0] == '2':
        c = d.popleft()
        N -= 1
        M = (M-c*pow(10,N,mod)) % mod
    if q[0] == '3':
        print(M)