N = int(input())
dai = [0]*(2*N+2)
A = list(map(int,input().split()))

for i in range(N):
    ameba, num = A[i], i+1
    dai[2*num] = dai[ameba] + 1
    dai[2*num+1] = dai[ameba] + 1

for i in range(1,2*N+2):
    print(dai[i])