A , B = map(int, input().split())
if A == 0 and B > 0:
  print('Silver')
elif B == 0 and A > 0:
  print('Gold')
elif A > 0 and B > 0:
  print('Alloy')