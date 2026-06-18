H, W = map(int,input().split())
Si, Sj = map(int,input().split())
Si, Sj = Si-1, Sj-1
List = ['']*H
for i in range(H):
    List[i] = input()
X = input()
for i in range(len(X)):
    if X[i] == 'L':
        if Sj != 0:
            if List[Si][Sj-1] == '.':
                Sj -= 1
    if X[i] == 'R':
        if Sj != W-1:
            if List[Si][Sj+1] == '.':
                Sj += 1
    if X[i] == 'U':
        if Si != 0:
            if List[Si-1][Sj] == '.':
                Si -= 1
    if X[i] == 'D':
        if Si != H-1:
            if List[Si+1][Sj] == '.':
                Si += 1
print(Si+1,Sj+1)