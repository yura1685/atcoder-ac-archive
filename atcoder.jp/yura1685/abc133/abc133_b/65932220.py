def square(n):
    return int(n**(1/2)) == n**(1/2)

def distance(a,b):
    dis = 0
    for i in range(len(a)):
        dis += (a[i]-b[i])**2
    return dis

N, D = map(int,input().split())
X = ['']*N

for i in range(N):
    X[i] = list(map(int,input().split())) # type: ignore

ans = 0
for i in range(N-1):
    for j in range(i+1,N):
        ans += square(distance(X[i],X[j]))
print(ans)