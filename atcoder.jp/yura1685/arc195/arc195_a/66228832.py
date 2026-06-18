N, M = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

cnt = 0
ansm = []
for i in range(N):
    if cnt == M:
        break
    if A[i] == B[cnt]:
        ansm.append(i)
        cnt += 1

if len(ansm) < M:
    print('No')
    exit()

cnt = M-1
ansM = []
for i in range(N):
    if cnt == -1:
        break
    if A[N-i-1] == B[cnt]:
        ansM.append(N-i-1)
        cnt -= 1
ansM.sort()

print('Yes' if ansm != ansM else 'No')