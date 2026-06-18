n,m,x,t,d=map(int,input().split())
n=x-m
print(t if m>=x else t-n*d)