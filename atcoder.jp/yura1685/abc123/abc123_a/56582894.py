c = []
for _ in range(5):
    c.append(int(input()))
k = int(input())
for i in range(5):
    for j in range(i,5):
        if c[j] - c[i] > k:
            print(':(')
            exit()
print('Yay!')