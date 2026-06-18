N, M = map(int, input().split())
ans = [0] * (M+1)
for _ in range(N):
    A, B = map(int, input().split())
    ans[A] -= 1
    ans[B] += 1
    
for i in range(1, M+1):
    print(ans[i])