N, M = map(int,input().split())
A = list(map(int,input().split()))

vote = [0]*(N+1)
m = 0

for a in A:
    vote[a] += 1
    if vote[a] > vote[m] or (vote[a] == vote[m] and a < m):
        m = a
    print(m)