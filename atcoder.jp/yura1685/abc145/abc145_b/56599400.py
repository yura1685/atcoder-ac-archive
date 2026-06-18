n=int(input())
if int(n)%2!=0:
    print('No')
    exit()
s=input()
if s[n//2:]==s[:n//2]:
    print('Yes')
else:
    print('No')