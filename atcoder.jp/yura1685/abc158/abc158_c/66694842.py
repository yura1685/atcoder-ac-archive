A, B = map(int, input().split())

for n in range(1,10000):
    if 108*n//100 - n == A and 110*n//100 - n == B:
        print(n)
        exit()
print(-1)