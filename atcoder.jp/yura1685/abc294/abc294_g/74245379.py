from atcoder.lazysegtree import LazySegTree
f=lambda x,y:x+y;I=input;L=lambda:map(int,I().split());n=int(I());g=[[]for _ in' '*n];E=[]
for _ in' '*(n-1):u,v,w=L();u-=1;v-=1;g[u]+=[(v,w)];g[v]+=[(u,w)];E+=[(u,v)]
K=n.bit_length();P=[[-1]*n for _ in' '*K];D,G,B,H,s=[0]*n,[-1]*n,[-1]*n,[0]*n,0;S=[(0,-1,0,0,1)]
while S:
 u,p,w,d,m=S.pop()
 if m:S+=[(u,p,w,d,0)];G[u]=s;H[u]=(H[p]if~p else 0)+w;D[u]=d;P[0][u]=p;[S.append((v,u,W,d+1,1))for v,W in g[u]if v!=p]
 else:B[u]=s
 s+=1
for k in range(K-1):
 for i in range(n):
  if~P[k][i]:P[k+1][i]=P[k][P[k][i]]
def J(u,v):
 if D[u]<D[v]:u,v=v,u
 for k in range(K):
  if(D[u]-D[v])>>k&1:u=P[k][u]
 if u==v:return u
 for k in range(K-1,-1,-1):
  if P[k][u]!=P[k][v]:u=P[k][u];v=P[k][v]
 return P[0][u]
X=[0]*(2*n)
for i in range(n):X[G[i]]=X[B[i]]=H[i]
z=LazySegTree(f,0,f,f,0,X)
for _ in' '*int(I()):
 q,x,y=L()
 if q<2:u,v=E[x-1];c=v if D[v]>D[u] else u;z.apply(G[c],B[c]+1,y-(z.get(G[c])-z.get(G[P[0][c]])))
 else:u,v=x-1,y-1;l=J(u,v);print(z.get(G[u])+z.get(G[v])-2*z.get(G[l]))