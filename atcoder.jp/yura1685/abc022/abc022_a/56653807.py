N, S, T = map(int,input().split())
W_now = int(input())
best_body = 0
if S <= W_now <= T:
    best_body += 1
for i in range(N-1):
    W_now += int(input())
    if S <= W_now <= T:
        best_body += 1
print(best_body)