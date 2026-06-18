a,b,c,d,e,f,x=map(int,input().split())
y=(x//(a+c)*a+min(a,x%(a+c)))*b
z=(x//(d+f)*d+min(d,x%(d+f)))*e
print("Takahashi" if y>z else "Aoki" if y<z else "Draw")