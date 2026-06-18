N = int(input())
A = list(map(int,input().split()))

left = [1]
right = [1]
for i in range(1,N):
    left.append(min(left[-1]+1,A[i]))
    right.append(min(right[-1]+1,A[N-i-1]))
right.reverse()

ans = 0
for i in range(N):
    ans = max(ans,min(left[i],right[i]))
print(ans)