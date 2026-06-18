N = int(input())
t, a = 0, 0
for _ in range(N):
    s = input()
    t += s.count('R')
    a += s.count('B')
if t > a: print('TAKAHASHI')
elif a > t: print('AOKI')
else: print('DRAW')