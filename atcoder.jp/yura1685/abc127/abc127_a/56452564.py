a, b = map(int,input().split())
print(b-(a<=12)*b//2-(a<=5)*b//2)