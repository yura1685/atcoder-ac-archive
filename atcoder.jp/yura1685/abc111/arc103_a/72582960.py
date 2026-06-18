from collections import Counter
N = int(input())
S = list(map(int,input().split()))
S1, S2 = Counter(S[0::2]), Counter(S[1::2])

M1 = [(0,1685),(0,1685)]
for s, cnt in S1.items():
    if M1[1] < (cnt,s):
        M1 = [M1[1], (cnt,s)]
    elif M1[0] < (cnt,s):
        M1[0] = (cnt,s)

M2 = [(0,1685),(0,1685)]
for s, cnt in S2.items():
    if M2[1] < (cnt,s):
        M2 = [M2[1], (cnt,s)]
    elif M2[0] < (cnt,s):
        M2[0] = (cnt,s)

if M1[1][1] != M2[1][1]:
    print(N - M1[1][0] - M2[1][0])

else:
    print(min(N - M1[0][0] - M2[1][0], N - M1[1][0] - M2[0][0]))