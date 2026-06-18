import bisect

N,A,B = map(int,input().split())
S = input()

wa = 0
wb = 0
ra = [0]
rb = [0]
for s in S:
    if s == 'a':
        wa += 1
    elif s == 'b':
        wb += 1
    ra.append(wa)
    rb.append(wb)

ans = 0
for l in range(1, N + 1):
    a_need = ra[l - 1] + A
    b_need = rb[l - 1] + B

    # r の範囲を探索
    a_l = bisect.bisect_left(ra, a_need, l)
    b_h = bisect.bisect_left(rb, b_need, l)

    ans += max(0, b_h - a_l)

print(ans)