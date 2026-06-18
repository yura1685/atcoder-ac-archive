N = int(input())
A = sorted((int(t),i+1) for i, t in enumerate(input().split()))
ans = [a[1] for a in A[:3]]
print(*ans)