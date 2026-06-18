Q = int(input())
stack = []
for _ in range(Q):
  S = input()
  if S == 'READ':
    book = stack.pop()
    print(book)
  else:
    stack.append(S)