N = int(input())
Q = list(map(int,input().split()))
A = list(map(int,input().split()))
B = list(map(int,input().split()))

ans = 0
for i in range(max(Q)+1):
    l = [Q[n]-i*A[n] for n in range(N)]
    if any([l[n] < B[n] for n in range(N)]):
        break
    b = [l[n]//B[n] if B[n] != 0 else float('inf') for n in range(N)]
    ans = max(ans,i+min(b))
print(ans)