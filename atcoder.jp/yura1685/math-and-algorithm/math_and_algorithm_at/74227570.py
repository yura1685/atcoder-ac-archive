N,M=int(input()),10**9
def t(a,b,c,d,e,f,g,h):
 return ((a*e+b*g)%M,(a*f+b*h)%M,(c*e+d*g)%M,(c*f+d*h)%M)
def f(a,b,c,d,n):
 if n==1: return (a, b, c, d)
 if n%2: return t(*f(*t(a,b,c,d,a,b,c,d),n//2),a,b,c,d)
 else: return f(*t(a,b,c,d,a,b,c,d),n//2)
print(f(1,1,1,0,N-1)[0])