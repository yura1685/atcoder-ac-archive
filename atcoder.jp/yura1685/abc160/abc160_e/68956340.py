X, Y, A, B, C = map(int,input().split())

R = sorted(map(int,input().split()))[A-X:]
G = sorted(map(int,input().split()))[B-Y:]
W = list(map(int,input().split()))

E = sorted(R+G+W)
print(sum(E[C:]))