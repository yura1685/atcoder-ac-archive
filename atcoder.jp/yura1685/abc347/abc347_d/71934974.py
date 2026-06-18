a, b, c = map(int,input().split())
A, B = a, b
C = bin(c)[2:]
C = '0'*(60-len(C)) + C

X = [0]*60
Y = [0]*60

W = 0
K = 0
for i in range(60):
    if C[i] == '0': # 両方とも一緒の個数
        W += 1
    else:
        K += 1 # 数字が異なる個数

if a + b < K:
    print(-1)
    exit()

pl = a + b - K # 両方とも 1 にする個数
if pl % 2 != 0:
    print(-1)
    exit()

a -= pl//2
b -= pl//2

for i in range(60):
    if C[i] == '0':
        if pl > 0:
            X[i], Y[i] = 1, 1
            pl -= 2
    else:
        if a > 0:
            X[i] = 1
            a -= 1
        elif b > 0:
            Y[i] = 1
            b -= 1

X = [str(i) for i in X]
Y = [str(i) for i in Y]

s, t = int(''.join(X),2), int(''.join(Y),2)

if s^t != c or a or b or (s.bit_count() != A) or (t.bit_count() != B):
    print(-1)
    exit()
    
print(s,t)