N = int(input())
dict = [[-1] * (N + 1) for _ in range(N+1)]
lst = []
i = 0
cnt = 1
while pow(2, i) <= N:
    haba = pow(2, i)
    for j in range(N - haba + 1):
        l, r = j + 1, j + haba
        lst.append((l, r))
        dict[l][r] = cnt
        cnt += 1
    i += 1

print(len(lst))
for l, r in lst:
    print(l, r)

Q = int(input())
for _ in range(Q):
    I = input().split()
    L, R = int(I[0]), int(I[1])
    haba = R - L + 1
    i = 1
    while i <= haba:
        i *= 2
    i //= 2
    print(dict[L][L+i-1], dict[R-i+1][R])