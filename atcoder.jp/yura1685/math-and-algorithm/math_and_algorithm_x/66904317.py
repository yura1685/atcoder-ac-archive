N = int(input())
score = 0
for _ in range(N):
    P, Q = map(int,input().split())
    score += Q/P

print(score)