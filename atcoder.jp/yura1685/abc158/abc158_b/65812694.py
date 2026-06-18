N, A, B = map(int,input().split())
blue = A*(N//(A+B))
N -= (A+B)*(N//(A+B))
print(blue + min(A,N))