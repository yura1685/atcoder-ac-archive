N = int(input())
S = input()
A = [i for i in range(2*N) if S[i] == 'A']

ans1 = 0
ans2 = 0
for i in range(N):
    ans1 += abs(A[i] - 2*i)
    ans2 += abs(A[i] - (2*i+1))

print(min(ans1,ans2))