N = int(input())
glid = [list(input()) for _ in range(N)]
glid.reverse()
hoge = list(zip(*glid))
for i in hoge:
    print(''.join(i))