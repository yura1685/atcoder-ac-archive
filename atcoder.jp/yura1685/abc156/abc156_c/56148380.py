N = int(input())
X = sorted(list(map(int,input().split())))

L = []

if max(X) == min(X):
    print(0)
    exit()

for i in range(X[0],X[-1]):
    ans = 0
    for k in range(len(X)):
        ans += (X[k]-i)**2
    L.append(ans)
print(min(L))