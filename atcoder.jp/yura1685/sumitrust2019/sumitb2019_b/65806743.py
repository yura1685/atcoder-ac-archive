N = int(input())
m = 25*N//27
while m * 1.08 < N + 1:
    if int(m*27 // 25) == N:
        print(m)
        exit()
    m += 1
print(':(')