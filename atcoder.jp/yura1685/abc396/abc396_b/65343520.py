Q = int(input())
card = [0]*100
for i in range(Q):
  q = input()
  if q == '2':
    print(card[0])
    card = card[1:]
  else:
    card = [int(q[2:])] + card