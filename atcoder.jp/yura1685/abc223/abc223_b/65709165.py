S = input()
n = len(S)
ans_min, ans_max = S, S
S += S
for i in range(n):
    ans_min = min(ans_min,S[i:i+n])
    ans_max = max(ans_max,S[i:i+n])
print(ans_min)
print(ans_max)