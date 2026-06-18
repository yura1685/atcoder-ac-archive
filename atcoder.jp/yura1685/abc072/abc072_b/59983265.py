s = input()
c = ''
x = 1
while True:
    if 2*x-1 <= len(s):
        c += s[2*x-2]
    else:
        break
    x += 1
print(c)