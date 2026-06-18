V, A, B, C = map(int,input().split())
roop = 0
while V >= 0:
    if roop == 0:
        V -= A
        roop = 1
    elif roop == 1:
        V -= B
        roop = 2
    else:
        V -= C
        roop = 0
if roop == 0:
    print('T')
elif roop == 1:
    print('F')
else:
    print('M')