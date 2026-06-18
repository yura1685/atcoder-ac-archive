n,k,a=map(int,input().split())
p=a

for i in range(k-1):
    if p==n:
        p=1
    else:
        p+=1

print(p)