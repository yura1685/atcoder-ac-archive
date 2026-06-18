N = int(input())
H = list(map(int, input(). split()))
H1 = H[0]
for i in range(N):
    if H[i] > H1:
        print(i+1)
        break
if H1 == max(H):
    print(-1)