N = int(input())
c1 = [0]
c2 = [0]
for _ in range(N):
    c, p = map(int,input().split())
    if c == 1:
        c1.append(p)
        c2.append(0)
    else:
        c1.append(0)
        c2.append(p)

score1, score2 = 0, 0
f1, f2 = [], []
for i in range(N+1):
    score1 += c1[i]
    score2 += c2[i]
    f1.append(score1)
    f2.append(score2)

Q = int(input())
for _ in range(Q):
    l, r = map(int,input().split())
    print(f1[r]-f1[l-1], f2[r]-f2[l-1])