N, A, B = map(int,input().split())
H = [int(input()) for _ in range(N)]
D = A - B

l, r = 0, 10**9
while r - l > 1:
    mid = (r+l)//2
    X = sum(max((h-mid*B+D-1)//D,0) for h in H)
    if X > mid:
        l = mid
    else:
        r = mid

print(r)