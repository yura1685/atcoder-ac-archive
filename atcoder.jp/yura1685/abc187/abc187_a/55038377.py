A, B = map(int, input(). split())
def S(x):
    return (x//100 + (x-x//100*100)//10 + x%10)
a = S(A)
b = S(B)
print(max(a, b))