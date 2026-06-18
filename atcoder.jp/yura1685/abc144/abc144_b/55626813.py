N = int(input())
for a in range(1,10):
    if N % a == 0:
        if len(str(N//a)) == 1:
            print('Yes')
            exit()
print('No')