T = int(input())
def f(n):
    if n % 2 == 1:
        return 'Odd'
    elif n % 4 == 0:
        return 'Even'
    else:
        return 'Same'
    
for _ in range(T):
    print(f(int(input())))