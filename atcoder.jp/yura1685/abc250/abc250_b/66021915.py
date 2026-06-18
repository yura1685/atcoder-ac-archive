N, A, B = map(int,input().split())
x = ['.#','#.']
ans = []
for i in range(N*A):
    c = ''
    for j in range(N*B):
        c += x[(i//A)%2][(j//B)%2]
    ans.append(c)

for i in ans:
    print(i)