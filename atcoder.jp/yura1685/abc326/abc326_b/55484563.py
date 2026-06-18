N = int(input())
def number326(n):
    a = n // 100
    b = (n - 100*a) // 10
    c = n - 100*a - 10*b
    if a*b == c:
        print(n)
        exit()
for i in range(N,999):
    number326(i)