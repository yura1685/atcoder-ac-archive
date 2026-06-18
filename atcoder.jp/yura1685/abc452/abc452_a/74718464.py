s = {107, 303, 505, 707, 909}
M, D = map(int, input().split())
print('Yes' if 100 * M + D in s else 'No')