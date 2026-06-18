N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
B.append(0)
A.sort(reverse=True); B.sort(reverse=True)

flag = 0
for i in range(N):
    if flag:
        c = i-1
        if A[i] > B[c]:
            print(-1)
            exit()
    if A[i] > B[i] and not flag:
        ans = A[i]
        flag = 1
print(ans)