b = [list(map(int, input().split())) for _ in range(2)]
c = [list(map(int, input().split())) for _ in range(3)]

def dfs(L, t):
    if t == 9:
        taro, hana = 0, 0
        for i in range(2):
            for j in range(3):
                if L[i][j] == L[i+1][j]:
                    taro += b[i][j]
                else:
                    hana += b[i][j]
        for i in range(3):
            for j in range(2):
                if L[i][j] == L[i][j+1]:
                    taro += c[i][j]
                else:
                    hana += c[i][j]
        return taro, hana

    if t % 2 == 0:
        taro, hana = 0, 0
        for i in range(3):
            for j in range(3):
                if L[i][j] == 0:
                    L[i][j] = 1
                    x, y = dfs(L, t+1)
                    L[i][j] = 0
                    taro, hana = max((taro, hana), (x, y))
        return taro, hana
    
    else:
        taro, hana = 0, 0
        for i in range(3):
            for j in range(3):
                if L[i][j] == 0:
                    L[i][j] = 2
                    x, y = dfs(L, t+1)
                    L[i][j] = 0
                    hana, taro = max((hana, taro), (y, x))
        return taro, hana

taro, hana = dfs([[0, 0, 0], [0, 0, 0], [0, 0, 0]], 0)

print(taro)
print(hana)