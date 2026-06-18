s=input().split()
a=0
b=0
c=0
if s[0]=="<":
    b+=1
else:
    a+=1
if s[1]=="<":
    c+=1
else:
    a+=1
if s[2]=="<":
    c+=1
else:
    b+=1
x=[(a,"A"),(b,"B"),(c,"C")]
x.sort()
print(x[1][1])