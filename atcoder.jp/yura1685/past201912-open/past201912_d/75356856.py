N = int(input())
L = [1] + [0] * N
for _ in range(N):
    a = int(input())
    L[a] += 1
    
if 0 in L:
    print(L.index(2), L.index(0))
else:
    print('Correct')