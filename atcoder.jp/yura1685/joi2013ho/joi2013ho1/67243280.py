N = int(input())
L = input().split()
L = [L[0]] + L + [L[-1]]

combo = [i for i in range(N+1) if L[i] == L[i+1]]
A = [combo[i+1] - combo[i] for i in range(len(combo)-1)]
A = [0] + A + [0]

ans = 0
for i in range(1,len(A)-1):
    ans = max(ans,A[i-1]+A[i]+A[i+1])
    
print(ans)