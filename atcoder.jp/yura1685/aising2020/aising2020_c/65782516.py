N = int(input())
c = [0]*(N+1)
for x in range(1,100):
    for y in range(1,100):
        for z in range(1,100):
            d = x*x + y*y + z*z + x*y + y*z + z*x
            if d > N:
                break
            c[d] += 1

for i in range(1,N+1):
    print(c[i])