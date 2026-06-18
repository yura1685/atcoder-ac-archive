a, b, c, d = map(int,input().split())
takahashi = b / a
aoki = d / c
if takahashi > aoki:
    print("TAKAHASHI")
elif takahashi < aoki:
    print("AOKI")
else:
    print("DRAW")