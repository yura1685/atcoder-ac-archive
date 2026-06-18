N = int(input())
A = list(map(int,input().split()))
a = min(A)
ans = 1
while len(A) != 0:
    if a == min(A):
        A.remove(a)
        if len(A) == 0:
            break
    if a != min(A):
        a = min(A)
        ans += 1
print(ans)