N = int(input())
Bone = []
for _ in range(N):
    a, b = map(int, input().split())
    Bone.append([a, b-1])
X = [set() for _ in range(N)]
M = int(input())
S = []
for _ in range(M):
    s = input()
    S.append(s)
    lens = len(s)
    for i in range(N):
        a, b = Bone[i]
        if a == lens:
            X[i].add(s[b])

for s in S:
    if len(s) != N:
        print('No')
        continue
    if all([s[i] in X[i] for i in range(N)]):
        print('Yes')
    else:
        print('No')