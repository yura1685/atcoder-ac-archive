N, S, T = map(int,input().split())
A = list(map(int,input().split()))
print('Yes' if 60*S + sum(A) <= 60*T else 'No')