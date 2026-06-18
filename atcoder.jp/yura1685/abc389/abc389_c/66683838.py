Q = int(input())
query = [list(map(int,input().split())) for _ in range(Q)]

snake = []
ruisekiwa = [0]
for q in query:
    if q[0] == 1:
        ruisekiwa.append(ruisekiwa[-1]+q[1])
        snake.append(q[1])

cnt = 0
minus = 0

for q in query:
    if q[0] == 2:
        minus += snake[cnt]
        cnt += 1
    elif q[0] == 3:
        print(ruisekiwa[q[1]+cnt-1] - minus)