N = int(input())
d = {'M':0, 'A':1, 'R':2, 'C':3, 'H':4}
c = [0]*5
for _ in range(N):
    S = input()
    if S[0] in d:
        c[d[S[0]]] += 1

ans = 0
for i in range(3):
    for j in range(i+1,4):
        for k in range(j+1,5):
            ans += c[i]*c[j]*c[k]

print(ans)