n = int(input())

tri = [0,0,0,1]
for _ in range(n-2):
    x = (tri[-1]+tri[-2]+tri[-3]) % 10007
    tri.append(x)

print(tri[n])