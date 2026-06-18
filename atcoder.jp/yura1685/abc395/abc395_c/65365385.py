N = int(input())
A = list(map(int,input().split()))
last = [0]*(max(A)+1)
Len = []

for i in range(N):
    if last[A[i]] != 0:
        Len.append(i + 1 - last[A[i]] + 1)
    last[A[i]] = i+1
print(min(Len) if Len != [] else -1)