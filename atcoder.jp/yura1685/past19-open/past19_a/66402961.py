X, H, M = map(int,input().split())

if M < X:
    print(X-M)
else:
    print(X+60-M)