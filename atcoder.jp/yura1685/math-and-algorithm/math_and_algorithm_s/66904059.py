N = int(input())
A = list(map(int,input().split()))

c = [A.count(i) for i in range(1,4)]
print(sum([c[i]*(c[i]-1) for i in range(3)])//2)