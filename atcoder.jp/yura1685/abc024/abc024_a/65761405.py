A, B, C, K = map(int,input().split())
S, T = map(int,input().split())
print(S*A+T*B-C*(S+T)*(S+T>=K))