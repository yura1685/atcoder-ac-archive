N = int(input())
A = list(map(int,input().split()))

c = [0]*100002
for i in A:
    c[i] += 1

now_max = 0
for i in range(100000):
    m = c[i] + c[i+1] + c[i+2]
    now_max = max(now_max,m)
print(now_max)