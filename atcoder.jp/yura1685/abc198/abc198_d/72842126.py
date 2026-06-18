from itertools import permutations

S1, S2, S3 = input(), input(), input()
S = set(S1+S2+S3)
N = len(S)
if N >= 11: exit(print('UNSOLVABLE'))

d = dict()
cnt = 0
for s in S:
    if not d.get(s):
        d[s] = cnt
        cnt += 1

S1 = [d[s] for s in S1]
S2 = [d[s] for s in S2]
S3 = [d[s] for s in S3]

for P in permutations([str(i) for i in range(10)]):
    if P[S1[0]] == '0' or P[S2[0]] == '0' or P[S3[0]] == '0':
        continue
    N1 = int("".join(P[s] for s in S1))
    N2 = int("".join(P[s] for s in S2))
    N3 = int("".join(P[s] for s in S3))
    if N1 + N2 == N3:
        print(N1); print(N2); print(N3)
        exit()

print('UNSOLVABLE')