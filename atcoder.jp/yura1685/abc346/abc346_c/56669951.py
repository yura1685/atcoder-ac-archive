N, K = map(int,input().split())
A = list(map(int,input().split()))
sum_max = K*(K+1)//2
d = set(A)
i = 0
for i in d:
    if i <= K:
        sum_max -= i
print(sum_max)