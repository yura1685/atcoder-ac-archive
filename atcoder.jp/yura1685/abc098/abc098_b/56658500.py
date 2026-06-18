N = int(input())
S = input()
ans = 0
for i in range(1,N):
    X, Y = S[:i], S[i:]
    same = len((set(X) | set(Y)) - (set(X) - set(Y)) - (set(Y) - set(X)))
    ans = max(ans, same)
print(ans)