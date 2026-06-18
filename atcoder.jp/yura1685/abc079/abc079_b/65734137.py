L = [2,1] + [0]*100
N = int(input())
for i in range(100):
    L[i+2] = L[i] + L[i+1]
print(L[N])