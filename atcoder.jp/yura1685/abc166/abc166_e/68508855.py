from collections import Counter

N = int(input())
A = list(map(int,input().split()))
# i, j であって，j-i = A[i] + A[j]  <->  i + A[i] = j - A[j] (i < j)
# となるものの総数に等しい
B = [j - A[j] for j in range(N)]
C = Counter(B)

ans = 0
for i in range(N):
    ans += C[i + A[i]]

print(ans)