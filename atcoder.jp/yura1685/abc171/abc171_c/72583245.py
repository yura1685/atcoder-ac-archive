from numpy import base_repr

N = int(input())
i = 1
while True:
    if N - 26**i > 0:
        N -= 26**i
        i += 1
    else:
        break

X = str(base_repr(N-1,26))
X = '0'*(i-len(X)) + X

def f(x:str):
    try:
        n = int(x)
        return chr(n+97)
    except ValueError:
        return chr(ord(x)+42)
    
print(''.join(f(x) for x in X))