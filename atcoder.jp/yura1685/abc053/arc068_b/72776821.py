from collections import Counter
_=int(input())
A=[a%2 for a in Counter(input().split()).values()]
a1,a2=A.count(1),A.count(0)
print(a1+a2-a2%2)