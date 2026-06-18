N = int(input())
P = list(map(int,input().split()))
Q = [0]*N

num = 1
while max(P) != 0:
    n = max(P)
    count = P.count(n)
    for i in range(N):
        if P[i] == n:
            Q[i] = num
            P[i] = 0
    num += count

for i in Q: print(i)