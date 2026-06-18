s=input()
ans=False
for i in range(len(s)+1):
    for j in range(len(s)-i+1):
        t="A"*i+"B"*j+"C"*(len(s)-i-j)
        ans|=t==s
        
print("Yes" if ans else "No")