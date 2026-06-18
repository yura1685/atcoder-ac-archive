from atcoder.segtree import SegTree

N = int(input())
A = [0] + list(map(int,input().split())) + [0]
st = SegTree(min, N, A)
ans = 0

for i in range(1,N+1):
    a = A[i]
    ng, ok = 0, i
    while ok - ng > 1:
        mid = (ng + ok) // 2
        if st.prod(mid,i+1) == a:
            ok = mid
        else:
            ng = mid
    L = ok

    ok, ng = i, N+1
    while ng - ok > 1:
        mid = (ng + ok) // 2
        if st.prod(i, mid+1) == a:
            ok = mid
        else:
            ng = mid
    R = ok
    
    ans += a * (i - L + 1) * (R - i + 1)

print(ans)