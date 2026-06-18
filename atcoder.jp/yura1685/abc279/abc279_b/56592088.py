t = input()
s = input()
for i in range(len(t)-len(s)+1):
    if s == t[i:i+len(s)]:
        print('Yes')
        exit()
print('No')