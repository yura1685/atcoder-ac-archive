N = int(input())
S = input()
ans = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if S[i] == 'E' and S[j] == 'G' and S[k] == 'F':
                ans += 1
print(ans)