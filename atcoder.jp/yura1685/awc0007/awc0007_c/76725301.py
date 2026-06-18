N, K = map(int, input().split())
A = [(a, -i-1) for i, a in enumerate(map(int, input().split()))]
while len(A) > 1:
    A = [max(A[i:i+K]) for i in range(0, len(A), K)]
print(-A[0][1])