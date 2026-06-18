A, B, C = map(int,input().split())
M = max(A,B,C)
s = [M-A,M-B,M-C]

print(sum(s)//2 if sum(s) % 2 == 0 else sum(s)//2+2)