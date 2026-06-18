X, Y = map(int,input().split())

def rev(S):
    S = str(S)
    return int(S[::-1])



for _ in range(8):
    N = rev(Y+X)
    Y, X = N, Y

print(Y)