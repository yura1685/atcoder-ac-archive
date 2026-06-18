N, S = map(int,input().split())
T = [0] + list(map(int,input().split()))

for i in range(N):
    if T[i] + S < T[i+1]:
        print('No')
        exit()
print('Yes')