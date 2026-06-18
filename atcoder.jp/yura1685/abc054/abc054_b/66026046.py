N, M = map(int,input().split())
A = [input() for _ in range(N)]
B = [input() for _ in range(M)]

for h in range(N-M+1):
    for w in range(N-M+1):
        flag = False
        for dh in range(M):
            for dw in range(M):
                if A[h+dh][w+dw] != B[dh][dw]:
                    flag = True
                    break
            if flag:
                break    
        if not flag:
            print('Yes')
            exit()
print('No')