N,M=map(int,input().split())
H=list(map(int,input().split()))

ans=0
for h in H:
  M-=h
  if(M>=0):
    ans+=1
  else:
    break
  
print(ans)