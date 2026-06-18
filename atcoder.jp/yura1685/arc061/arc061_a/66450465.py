from itertools import product

S = input()
x = list(product([0,1],repeat=len(S)-1))

ans = 0
for c in x:
    hoge = ''
    for i in range(len(c)):
        hoge += S[i]
        if c[i] == 1:
            hoge += '+'
    hoge += S[-1]
    ans += sum(list(map(int,hoge.split('+'))))

print(ans)