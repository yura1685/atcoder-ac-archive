from atcoder.string import suffix_array, lcp_array

S = input()
sa = suffix_array(S)

ans = len(S) * (len(S)+1) // 2
for x in lcp_array(S, sa):
    ans -= x

print(ans)