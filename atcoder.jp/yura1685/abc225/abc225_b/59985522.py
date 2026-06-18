N = int(input())
tree = [0]*N
for _ in range(N-1):
    a, b = map(int,input().split())
    tree[a-1] += 1
    tree[b-1] += 1

if max(tree) == N-1:
    print('Yes')
else:
    print('No')