H, W = map(int,input().split())
alp = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
snake = ['']*H
for i in range(H):
    snake[i] = list(map(str,input().split()))
for i in range(H):
    for j in range(W):
        if snake[i][j] == 'snuke':
            eigo = alp[j]
            print(eigo+str(i+1))
            exit()