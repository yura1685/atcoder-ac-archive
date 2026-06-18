from atcoder.segtree import SegTree

N = int(input())
H = [int(input()) for _ in range(N)]
st = SegTree(max, 0, H)

mr = [0] * N
for i in range(N):
    c = st.max_right(i, lambda x: x <= H[i])
    mr[i] = c - i - 1

ml = [0] * N
for i in range(N):
    c = st.min_left(i, lambda x: x <= H[i])
    ml[i] = i - c

for i in range(N):
    print(ml[i] + mr[i])