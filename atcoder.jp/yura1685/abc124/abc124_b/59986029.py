N = int(input())
H = list(map(int,input().split()))
now_max = 0
nice_view = 0
for i in range(N):
    if now_max <= H[i] :
        nice_view += 1
        now_max = H[i]
print(nice_view)