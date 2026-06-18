N, K, Q = map(int,input().split())
point = [0]*(N+1)
for quiz in range(Q):
    A = int(input())
    point[A] += 1
for i in range(1,N+1):
    if point[i] > Q-K:
        print('Yes')
    else:
        print('No')