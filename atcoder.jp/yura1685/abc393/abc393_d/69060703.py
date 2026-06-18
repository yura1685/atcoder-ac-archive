N = int(input())
S = input()
c = S.count('1')
mid = (c+1)//2

cnt = 0
for i in range(N):
    if S[i] == '1':
        cnt += 1
    if cnt == mid:
        I = i
        break


L, R = [], []
for i in range(1,I+1):
    if S[I-i] == '1':
        L.append(i)

for i in range(1,N-I):
    if S[I+i] == '1':
        R.append(i)

ans = 0
for i in range(len(L)):
    ans += L[i] - i - 1
for i in range(len(R)):
    ans += R[i] - i - 1

print(ans)