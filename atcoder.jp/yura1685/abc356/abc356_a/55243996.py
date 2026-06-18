A,B,C=map(int,input().split(" "))
L=[]
for i in range(A):
  L.append(i+1)
for i in range(C-B+1):
  L[B+i-1]=C-i
print(*L)