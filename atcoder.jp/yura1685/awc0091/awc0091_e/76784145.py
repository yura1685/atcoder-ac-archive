from atcoder.segtree import SegTree

N, Q = map(int, input().split())
lst = []
for _ in range(N):
    D, B = input().split()
    B = int(B)
    if D == 'R':
        lst.append((B, B))
    else:
        lst.append((-B, -B))

def op(a, b):
    a_sum, a_pref = a
    b_sum, b_pref = b
    return (a_sum + b_sum, max(a_pref, a_sum + b_pref))

e = (0, -10**18)

st = SegTree(op, e, lst)

for _ in range(Q):
    q = input().split()
    if q[0] == '1':
        p, D, b = int(q[1]) - 1, q[2], int(q[3])
        if D == 'R':
            st.set(p, (b, b))
        else:
            st.set(p, (-b, -b))
    else:
        K = int(q[1])
        if st._d[1][1] < K:
            print(0)
        else:
            ng, ok = -1, N - 1
            while ok - ng > 1:
                mid = (ng + ok) // 2
                if st.prod(0, mid+1)[1] < K:
                    ng = mid
                else:
                    ok = mid
            print(ok + 1)