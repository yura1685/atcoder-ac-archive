from itertools import permutations

N, M = map(int,input().split())

S = [input() for _ in range(N)]
v = list(permutations(S))

def dif(a, b):
    dif = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            dif += 1
    return dif

def pat(S: tuple):
    n = len(S)-1
    ans = 0
    for i in range(n):
        ans += dif(S[i], S[i+1])
    if ans == N-1:
        return True
    else:
        return False
    
for x in v:
    if pat(x):
        print('Yes')
        exit()

print('No')