p = input()
c = 1685
for i in range(10):
    if p[i:i+12] == 'WBWBWWBWBWBW':
        c = i
        break
d = {0:'Do', 1:'Si', 3:'La', 5:'So', 7:'Fa', 8:'Mi'}
if c <= 8:
    print(d[c])
else:
    print('Re')