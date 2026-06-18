N, M = map(int,input().split())
A = list(map(int,input().split()))
c = []
for i in range(N):
    c.append(A[i])
    if len(set(c)) == M:
        print(N-i)
        exit()

print(0)