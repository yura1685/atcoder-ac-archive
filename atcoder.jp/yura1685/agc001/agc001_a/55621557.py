N = int(input())
L = list(map(int,input().split()))
niku = 0
for i in range(N):
    niku += min(L)
    L.remove(min(L))
    L.remove(min(L))
print(niku)