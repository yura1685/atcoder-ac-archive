N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

score = [0]*(N)
for i in range(N-1):
    if i == 0:
        score[A[i]-1] = max(score[A[i]-1], score[i]+100)
        score[B[i]-1] = max(score[B[i]-1], score[i]+150)        
    elif score[i] != 0:
        score[A[i]-1] = max(score[A[i]-1], score[i]+100)
        score[B[i]-1] = max(score[B[i]-1], score[i]+150)
        
print(score[-1])