N, P, Q = map(int, input(). split())
menu = list(map(int, input(). split()))
noticket = P
ticket = Q + min(menu)
print(min(noticket,ticket))