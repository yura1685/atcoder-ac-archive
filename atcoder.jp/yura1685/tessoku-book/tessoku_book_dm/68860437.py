N = int(input())
A = [int(x) % 100 for x in input().split()]
M = [0]*100
for a in A:
    M[a] += 1

ans = 0
for i in range(1,50):
    ans += M[i] * M[100-i]
ans += (M[50]*(M[50]-1) + M[0]*(M[0]-1))//2

print(ans)