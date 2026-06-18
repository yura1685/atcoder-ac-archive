N, K = map(int,input().split())
S = input()
can = 0
for i in range(N):
    if S[i] == 'o':
        can += 1
    if can == K:
        num = i + 1
        break
entry = S[:num] + 'x'*(N-num)
print(entry)