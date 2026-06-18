N = int(input())
S = input()

one = [i+1 for i in range(N) if S[i] == '1']
one.reverse()

cnt = 0
ans = ''
for n in one:
    ans += 'A'*n + 'B'*(n-1)
    cnt += 2*n-1

print(cnt)
print(ans)