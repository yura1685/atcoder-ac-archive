T = input()
U = input()
n = len(U)

for i in range(len(T)-n+1):
    ans = 0
    for j in range(n):
        if T[i+j] == '?':
            ans += 1
        elif T[i+j] == U[j]:
            ans += 1
        else:
            break
    if ans == n:
        print('Yes')
        exit()
print('No')