from collections import Counter

N = int(input())
S = input()
a, b, c = 0, 0, 0
AA, BB, CC = [0], [0], [0]

for s in S:
    if s == 'A':
        a += 1
    elif s == 'B':
        b += 1
    else:
        c += 1
    AA.append(a)
    BB.append(b)
    CC.append(c)

A_B = [AA[i] - BB[i] for i in range(N+1)]
B_C = [BB[i] - CC[i] for i in range(N+1)]
C_A = [CC[i] - AA[i] for i in range(N+1)]
ABC = [(A_B[i], B_C[i], C_A[i]) for i in range(N+1)]
X = Counter(A_B)
Y = Counter(B_C)
Z = Counter(C_A)
W = Counter(ABC)

ans = N * (N+1) // 2

for x in X.values():
    ans -= x * (x-1) // 2
for y in Y.values():
    ans -= y * (y-1) // 2
for z in Z.values():
    ans -= z * (z-1) // 2
for w in W.values():
    ans += w * (w-1)

print(ans)