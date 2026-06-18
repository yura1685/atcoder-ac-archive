H, W = map(int,input().split())
S = []

def c(i,j):
    return  S[i][j] == '#'

for _ in range(H):
    S.append('.'+input()+'.')
S = ['.'*(W+2)] + S + ['.'*(W+2)]
for h in range(1,H+1):
    for w in range(1,W+1):
        count = 0
        if S[h][w] == '.':
            count += c(h-1,w) + c(h,w-1) + c(h,w+1) + c(h+1,w)
            if count >= 2:
                print(h,w)
                exit()