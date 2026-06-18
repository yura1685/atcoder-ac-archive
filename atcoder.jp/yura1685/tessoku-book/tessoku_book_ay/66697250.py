Q = int(input())

book = []
for _ in range(Q):
    q = input().split()
    if q[0] == '1':
        book.append(q[1])
    elif q[0] == '2':
        print(book[-1])
    else:
        book.pop()
