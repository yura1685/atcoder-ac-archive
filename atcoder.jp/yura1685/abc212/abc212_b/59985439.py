p = input()
if p[0] == p[1] == p[2] == p[3]:
        print('Weak')
        exit()
num = '0123456789012'
for i in range(10):
    if num[i:i+4] == p:
        print('Weak')
        exit()
print('Strong')