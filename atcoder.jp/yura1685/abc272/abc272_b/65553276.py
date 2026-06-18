N, M = map(int,input().split())

pair = []
for i in range(M):
    l = list(map(int,input().split()))
    k, m = l[0], l[1:]
    for i in range(k-1):
        for j in range(i+1,k):
            pair.append((m[i],m[j]))
c = len(set(pair))
print('Yes' if c == N*(N-1)//2 else 'No')