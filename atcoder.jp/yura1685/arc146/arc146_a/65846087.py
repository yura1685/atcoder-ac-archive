N = list(input())
A = list(map(int,input().split()))
A.sort(reverse=True)
a,b,c = str(A[0]), str(A[1]), str(A[2])
x = [a+b+c,a+c+b,b+c+a,b+a+c,c+a+b,c+b+a]
print(int(max(x)))