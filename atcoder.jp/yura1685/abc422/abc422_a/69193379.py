a, b = map(int, input().split('-'))
print(str(a)+'-'+str(b+1) if b < 8 else str(a+1)+'-'+str(1))