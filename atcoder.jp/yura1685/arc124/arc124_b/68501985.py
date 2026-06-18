N = int(input())
A = list(map(int,input().split()))
B = sorted(map(int,input().split()))
X = [A[0]^b for b in B]

ans = set()
for x in X:
    Y = [a^x for a in A]
    if B == sorted(Y):
        ans.add(x)

ans = sorted(ans)
print(len(ans))
for y in ans:
    print(y)