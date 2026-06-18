from collections import Counter

N = int(input())

dice = []

for _ in range(N):
    X = list(map(int,input().split()))
    dice.append((X[0],Counter(X[1:])))    

def P(l1,l2,A,B):
    C = A & B
    cnt = 0
    for c in C:
        cnt += A[c]*B[c]
    return cnt/(l1*l2)

ans = 0
for i in range(N-1):
    for j in range(i+1,N):
        l1, A = dice[i]
        l2, B = dice[j]
        ans = max(ans,P(l1,l2,A,B))

print(ans)