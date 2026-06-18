N = int(input())
S = input()

if S[0] != S[-1]:
    print(1)
    exit()

c = list(map(len, S.split(S[0])))

if max(c) > 1:
    print(2)
else:
    print(-1)