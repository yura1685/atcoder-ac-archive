K = int(input())
card = [0] + [K] * 9
S_in = input()
T_in = input()
s1, s2, s3, s4 = [int(s) for s in S_in[:4]]
t1, t2, t3, t4 = [int(t) for t in T_in[:4]]

for n in [s1, s2, s3, s4, t1, t2, t3, t4]: card[n] -= 1

def score(a, b, c, d, e):
    res = 0
    L = [0] * 10
    L[a] += 1; L[b] += 1; L[c] += 1; L[d] += 1; L[e] += 1
    for i in range(10):
        res += i * 10 ** L[i]
    return res

all, win = 0, 0
for taka in range(1,10):
    for aoki in range(1, 10):
        if taka == aoki:
            if card[taka] < 2:
                continue
            if score(s1,s2,s3,s4,taka) > score(t1,t2,t3,t4,aoki):
                win += card[taka] * (card[taka] - 1)
            all += card[taka] * (card[taka] - 1)
        else:
            if card[taka] < 1 or card[aoki] < 1:
                continue
            if score(s1,s2,s3,s4,taka) > score(t1,t2,t3,t4,aoki):
                win += card[taka] * card[aoki]
            all += card[taka] * card[aoki]

print(win / all)