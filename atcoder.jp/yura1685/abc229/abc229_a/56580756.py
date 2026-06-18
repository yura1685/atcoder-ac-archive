a = input()
b = input()

if a.count('.') + b.count('.') <= 1:
    print('Yes')
    exit()

if a[0] == b[0] or a[0] == a[1]:
    print('Yes')
    exit()

print('No')