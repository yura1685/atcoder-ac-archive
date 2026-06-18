N, K = map(int,input().split())
a = int(input())
b = int(input())
c = int(input())
sleep = a + b + c
for i in range(N-3):
    if sleep < K:
        print(i+3);exit()
    sleep -= a
    a, b, c = b, c, int(input())
    sleep += c
print(-1)