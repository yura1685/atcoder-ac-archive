N = int(input())
h = N // 3600
N -= h*3600
m = N // 60
N -= m*60
s = N
h, m, s = str(h),str(m),str(s)
if len(h) == 1:
    h = '0' + h
if len(m) == 1:
    m = '0' + m
if len(s) == 1:
    s = '0' + s
print(h+':'+m+':'+s)