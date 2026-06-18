s = input()
hug = 0
for i in range(len(s)//2):
    if s[i] != s[-1-i]:
        hug += 1
print(hug)