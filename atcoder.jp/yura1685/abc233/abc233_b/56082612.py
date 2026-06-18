L, R = map(int,input().split())
S = input()
T = S[L-1:R]
print(S[:L-1]+T[::-1]+S[R:])