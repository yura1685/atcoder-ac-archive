N = int(input())

V = []
sum_A, sum_T = 0, 0
for _ in range(N):
    A, T = map(int,input().split())
    sum_A += A
    V.append((2*A+T,A))
V.sort(reverse=True)

cnt = 0
while sum_T <= sum_A:
    S, A = V[cnt]
    sum_T += S-A
    sum_A -= A
    cnt += 1

print(cnt)