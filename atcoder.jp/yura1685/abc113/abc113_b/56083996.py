N = int(input())
T, A = map(int,input().split())
H = list(map(int,input().split()))
degree = []
for i in range(N):
    degree.append(T - H[i] * 0.006)
bestplace, point = 10**5, 0
for i in range(N):
    if bestplace > abs(A - degree[i]):
        bestplace, point = abs(A - degree[i]), i+1
print(point)