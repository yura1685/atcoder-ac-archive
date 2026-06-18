N, D = map(int,input().split())
snake = []
for i in range(N):
  snake.append(list(map(int,input().split())))
for k in range(1,D+1):
  maxk = 0
  for i in range(N):
    maxk = max(maxk,snake[i][0]*(snake[i][1]+k))
  print(maxk)