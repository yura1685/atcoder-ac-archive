N, a, b = map(str,input().split())
S = list(input())
for i in range(len(S)):
    if S[i] != a:
        S[i] = b
print(''.join(S))