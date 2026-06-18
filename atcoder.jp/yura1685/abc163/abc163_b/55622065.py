N, M = map(int,input().split())
A = list(map(int,input().split()))
homework = sum(A)
print(N - homework if N - homework >= 0 else -1)