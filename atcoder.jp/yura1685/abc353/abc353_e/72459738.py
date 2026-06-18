from collections import defaultdict
from statistics import mode

N = int(input())
S = input().split()

Mods = [16850000017, 168500000021, 1685000000011]

def solve(mod):
    cnt = defaultdict(int)
    ans = 0
    for s in S:
        hash = 0
        for t in s:
            hash = (hash * 314159 + ord(t)) % mod
            ans += cnt[hash]
            cnt[hash] += 1
    return ans

print(mode([solve(m) for m in Mods]))