N, S = map(int,input().split())
A = list(map(int,input().split()))

A.sort()
ans = [0]
for a in A:
    ans = list(set(ans))
    ans.sort()
    for i in range(len(ans)):
        n = a + ans[i]
        if n == S:
            print('Yes')
            exit()
        if n > S:
            break
        ans.append(n)
print('No')