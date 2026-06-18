N = int(input())
A = list(map(int,input().split()))
check = []

d = {}
for i in range(N):
    x = A[i]
    if d.get(x) == None:
        d[x] = [i]
    else:
        d[x].append(i)

B = set(A)
for i in B:
    if len(d[i]) == 1:
        check.append((i,d[i][0]))

check = sorted(check, reverse = True)
print(check[0][1]+1 if len(check) != 0 else -1)