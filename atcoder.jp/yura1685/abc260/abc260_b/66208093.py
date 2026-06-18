# クソ問をありがとう

N, X, Y, Z = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = [i for i in range(1,N+1)]
L = []
for i in range(N):
    L.append((A[i],-i-1))
L.sort(reverse=True)
gokaku = [-i[1] for i in L[:X]]
L = []
nopass = list(set(C) - set(gokaku))
for i in nopass:
    L.append((B[i-1],-i))
L.sort(reverse=True)
gokaku2 = [-i[1] for i in L[:Y]]
nopass = list(set(nopass) - set(gokaku2))
L = []
for i in nopass:
    L.append((A[i-1]+B[i-1],-i))
L.sort(reverse=True)
gokaku3 = [-i[1] for i in L[:Z]]

hoge = gokaku+gokaku2+gokaku3
hoge.sort()
for i in hoge:
    print(i)