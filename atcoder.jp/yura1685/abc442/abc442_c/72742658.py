N, M = map(int,input().split())
L = [N-1] * N
for _ in range(M):
    a, b = map(int,input().split())
    L[a-1] -= 1
    L[b-1] -= 1

print(*[i*(i-1)*(i-2)//6 for i in L])