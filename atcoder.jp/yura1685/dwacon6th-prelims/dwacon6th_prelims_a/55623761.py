N = int(input())
S, T = [], []
time = 0
for i in range(N):
    s, t = map(str,input().split())
    t = int(t)
    S.append(s)
    T.append(t)
X = input()
num = S.index(X)
for i in range(num+1,N):
    time += T[i]
print(time)