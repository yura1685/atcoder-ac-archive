N, K = map(int,input().split())
A = list(map(int,input().split()))

l, r = 0, max(A)
while r - l > 1:
    mid = (l+r)//2
    cnt = sum((a+mid-1)//mid - 1 for a in A)
    if cnt <= K:
      r = mid
    else:
      l = mid

print(r)