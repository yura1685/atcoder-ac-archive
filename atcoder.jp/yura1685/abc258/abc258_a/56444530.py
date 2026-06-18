K = int(input())
u = str(K%60)
if len(u) == 1:
    u = '0'+u
print(str(21+K//60)+':'+u)