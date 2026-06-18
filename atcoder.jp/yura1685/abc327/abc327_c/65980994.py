def sudoku(L):
    for i in range(1,10):
        if L.count(i) != 1:
            return False
    return True

s = [tuple(map(int,input().split())) for _ in range(9)]

for i in s:
    if not sudoku(i):
        print('No')
        exit()

t = list(zip(*s))
for i in t:
    if not sudoku(i):
        print('No')
        exit()

for x in [0,3,6]:
    for y in [0,3,6]:
        l = []
        for i in range(3):
            for j in range(3):
                l.append(s[x+i][y+j])
        if not sudoku(l):
            print('No')
            exit()

print('Yes')