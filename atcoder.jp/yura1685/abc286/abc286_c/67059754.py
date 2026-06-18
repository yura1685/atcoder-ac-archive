N, A, B = map(int,input().split())
S = input()

def f(x):
    dif = 0
    for i in range(N):
        if S[(i+x)%N] != S[(x-1-i)%N]:
            dif += 1
    return dif//2

ans = float('inf')
for cnt in range(N):
    ans = min(ans,A*cnt+B*f(cnt))

print(ans)
