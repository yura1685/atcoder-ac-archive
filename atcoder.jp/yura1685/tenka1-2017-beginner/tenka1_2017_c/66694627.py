N = int(input())

for h in range(1,3501):
    for n in range(h,3501):
        if (4*h*n-N*n-N*h) > 0 and (N*h*n) % (4*h*n-N*n-N*h) == 0:
            w = (N*h*n) // (4*h*n-N*n-N*h)
            print(h, n, w)
            exit()