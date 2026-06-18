from collections import defaultdict

H, W = map(int, input().split())
N = int(input())

rows = defaultdict(list)
for _ in range(N):
    A, B = map(int, input().split())
    rows[A].append(B)

case1 = 0
a_list = []

for row_idx in sorted(rows.keys()):
    bs = sorted(rows[row_idx])
    max_b = bs[-1]
    
    case1 += 2 * (max_b - 1)
    
    extended = [1] + bs + [W]
    max_gap = max(extended[j+1] - extended[j] for j in range(len(extended)-1))
    ai = 2 * (W - 1) - 2 * max_gap
    a_list.append(ai)

base_sum = sum(a_list)

deltas = sorted((W - 1) - ai for ai in a_list)

n = len(a_list)
prefix = [0] * (n + 1)
for i in range(n):
    prefix[i+1] = prefix[i] + deltas[i]

case2 = float('inf')
for k in range(2, n+1, 2):
    case2 = min(case2, base_sum + prefix[k])

print(min(case1, case2))
