X, Y, A, B = map(int,input().split())

cnt = 0
while True:
    if X*A <= X+B and X*A < Y:
        X *= A
        cnt += 1    
    else:
        break

cnt += (Y-1-X)//B

print(cnt)