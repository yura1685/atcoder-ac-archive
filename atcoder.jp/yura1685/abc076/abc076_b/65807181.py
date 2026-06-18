N = int(input())
K = int(input())
board = 1
for _ in range(N):
    board = min(2*board, board+K)
print(board)