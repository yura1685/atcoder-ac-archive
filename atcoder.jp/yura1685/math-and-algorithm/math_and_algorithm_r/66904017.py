N = int(input())
A = list(map(int,input().split()))

c = [A.count(100*i) for i in range(1,5)]
ans = c[0]*c[3] + c[1]*c[2]
print(ans)