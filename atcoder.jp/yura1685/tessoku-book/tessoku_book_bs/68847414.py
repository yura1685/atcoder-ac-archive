N = int(input())
A = sorted(map(int,input().split()))
B = sorted(map(int,input().split()))
print(sum(A[i]*B[-i-1] for i in range(N)))