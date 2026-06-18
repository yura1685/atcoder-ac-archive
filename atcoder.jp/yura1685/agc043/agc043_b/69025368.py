N = int(input())
A = input()
S = []
flag = False
for a in A:
    S.append(int(a)-1)
    if a == '2':
        flag = True

v2 = [0]
for k in range(1,N+1):
    cnt = 0
    while k % 2 == 0:
        k //= 2
        cnt += 1
    v2.append(v2[-1]+cnt)

xor = 0
for i in range(N):
    if (v2[N-1] - v2[N-1-i] - v2[i]) == 0:
        xor ^= S[i]

if xor % 2 == 1:
    exit(print(1))
if flag:
    exit(print(0))

T = [s//2 for s in S]

xor = 0
for i in range(N):
    if (v2[N-1] - v2[N-1-i] - v2[i]) == 0:
        xor ^= T[i]

if xor % 2 == 1:
    print(2)
else:
    print(0)