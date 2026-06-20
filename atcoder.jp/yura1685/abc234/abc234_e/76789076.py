X = input()
H = int(X[0])
N = len(X)
X = int(X)
ans = []
for h in range(H, 10):
    for d in range(-10, 11):
        Y = [h + d*i for i in range(N)]
        if min(Y) < 0 or max(Y) > 9:
            continue
        Z = int(''.join(map(str, Y)))
        if X <= Z:
            ans.append(Z)
ans.append(int('1'*(N+1)))
print(min(ans))