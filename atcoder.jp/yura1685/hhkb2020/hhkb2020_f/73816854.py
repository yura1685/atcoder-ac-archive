from collections import defaultdict

N = int(input())
_intervals = []
maxL, maxR = 0, 0
for _ in range(N):
    L, R = map(int,input().split())
    maxL, maxR = max(L, maxL), max(R, maxR)
    _intervals.append((L, R))

mod = 10**9 + 7

fact = 1
for i in range(1, N+2):
    fact = fact * i % mod

interval = []
prod = 1
all_prod = 1

for l, r in _intervals:
    if r > maxL:
        interval.append((l, r))
    else:
        prod = prod * (r-l) % mod
    all_prod = all_prod * (r-l) % mod

event = sorted(set(r for _, r in interval))

r_map = defaultdict(list)
for l, r in interval:
    r_map[r].append(l)

coeffs = [1]
for l, r in interval:
    new_coeffs = [0] * (len(coeffs) + 1)
    for i, c in enumerate(coeffs):
        new_coeffs[i+1] = (new_coeffs[i+1] + c) % mod
        new_coeffs[i] = (new_coeffs[i] - c * l) % mod
    coeffs = new_coeffs

cur_x = maxL
all_w = 0
cur_prod = prod

for next_x in event:
    if next_x > cur_x:
        term_sum = 0
        cur_pow = cur_x
        next_pow = next_x
        for k, c in enumerate(coeffs):
            pow_diff = (next_pow - cur_pow) % mod
            coef = fact * pow(k+1, -1, mod) % mod
            val = c * coef * pow_diff % mod
            term_sum = (term_sum + val) % mod
            if k < len(coeffs) - 1:
                cur_pow = cur_pow * cur_x % mod
                next_pow = next_pow * next_x % mod
        segment_val = term_sum * cur_prod % mod
        all_w = (all_w + segment_val) % mod
    
    cur_x = next_x

    if next_x in r_map:
        for l in r_map[next_x]:
            cur_prod = (cur_prod * (next_x - l)) % mod
            deg = len(coeffs) - 1
            new_coeffs = [0] * deg
            val = coeffs[deg]
            for i in range(deg-1, -1, -1):
                new_coeffs[i] = val
                val = (coeffs[i] + l * val) % mod
            coeffs = new_coeffs

term1 = maxR * fact * all_prod % mod
print((term1 - all_w) % mod)