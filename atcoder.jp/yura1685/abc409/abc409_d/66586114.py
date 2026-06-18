def solve(s):
    n = len(s)
    l = -1
    for i in range(n-1):
        if s[i] > s[i+1]:
            l = i
            break
    if l == -1:
        return s
    r = n
    for i in range(l+1,n):
        if s[l] < s[i]:
            r = i
            break
    return s[:l] + s[l+1:r] + s[l] + s[r:]

T = int(input())
for _ in range(T):
    N = int(input())
    S = input()
    print(solve(S))