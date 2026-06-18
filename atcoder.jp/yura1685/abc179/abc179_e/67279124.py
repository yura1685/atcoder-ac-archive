N, X, M = map(int,input().split())

cnt = [0]*M
seq = []
A = X
while True:
    if cnt[A] == 1:
        ind = seq.index(A)
        break
    cnt[A] += 1
    seq.append(A)
    A = (A*A) % M

mae = seq[:ind]
cir = seq[ind:]

t, s = len(mae), len(cir)

if t <= N:
    print(sum(mae) + sum(cir)*((N-t)//s) + sum(cir[:((N-t)%s)]))
else:
    print(sum(mae[:N]))