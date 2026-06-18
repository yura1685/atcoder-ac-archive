from functools import cmp_to_key
import bisect

def compare(a, b):
    if a[0] > b[0]:
        return 1
    if a[0] < b[0]:
        return -1
    if a[1] > b[1]:
        return -1
    if a[1] < b[1]:
        return 1
    return 0

N, M = map(int, input().split())
L = sorted([tuple(map(int, input().split())) for _ in range(M)], key=cmp_to_key(compare))
seq = [b for a, b in L]

LIS = [seq[0]]
for i in range(len(seq)):
    if seq[i] > LIS[-1]:
        LIS.append(seq[i])
    else:
        LIS[bisect.bisect_left(LIS, seq[i])] = seq[i]

print(len(LIS))