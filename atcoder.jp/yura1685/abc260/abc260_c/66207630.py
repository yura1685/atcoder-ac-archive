N, X, Y = map(int,input().split())

Red  = [1,0,0,0,0,0,0,0,0,0]
Blue = [0,0,0,0,0,0,0,0,0,0]

for i in range(N-1):
    Blue[i] += X*Red[i]
    Red[i+1] += Red[i]
    Red[i+1] += Blue[i]
    Blue[i+1] += Y*Blue[i]

print(Blue[N-1])