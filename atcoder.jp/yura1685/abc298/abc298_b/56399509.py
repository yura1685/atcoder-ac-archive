n = int(input())
a = []
b = []
for i in range(n):
    a_i = list(map(int, input().split()))
    a.append(a_i)
for i in range(0, n):
    b_i = list(map(int, input().split()))
    b.append(b_i)

b_onelist=set()
for i in range(n):
    for j in range(n):
        if b[i][j] == 1:
            b_onelist.add((i,j))

for i in range(0,4):
    a_new = [[1 for _ in range(n)] for _ in range(n)]
    for j in range(1,n+1):
        for k in range(1,n+1):
            a_new[j-1][k-1] = a[n-k][j-1]
    a = a_new
    one_list = set()
    for j in range(0,n):
        for k in range(0,n):
            if a_new[j][k] == 1:
                one_list.add((j,k))
    if one_list.issubset(b_onelist):
        print("Yes")
        exit()

print("No")
