H, W = map(int,input().split())

huton = 0
hotel = ['']*(H+2)

def ch(i,j):
    return hotel[i][j] == '.'

for i in range(1,H+1):
    hotel[i] = '#'+input()+'#'
hotel[0], hotel[-1] = '#'*(W+2), '#'*(W+2)

for i in range(1,H+1):
    for j in range(1,W+1):
        if hotel[i][j] == '.':
            huton += ch(i-1,j) + ch(i,j-1) + ch(i,j+1) + ch(i+1,j)

print(huton//2)