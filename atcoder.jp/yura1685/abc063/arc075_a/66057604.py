N = int(input())

S = [int(input()) for _ in range(N)]
T = []
c = [0]*10

for s in S:
    if s % 10 != 0:
        c[s % 10] += 1
        T.append(s)

hoge = 0
for i in range(10):
    hoge += i*c[i]

if hoge == 0:
    print(0)
elif hoge % 10 == 0:
    print(sum(S)-min(T))
else:
    print(sum(S))