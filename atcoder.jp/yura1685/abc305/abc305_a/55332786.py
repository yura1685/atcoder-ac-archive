N = int(input())
if N % 5 == 0 or N % 5 == 1 or N % 5 == 2:
    print(N-N%5)
elif N % 5 == 3 or N % 5 == 4:
    print(N//5*5+5)