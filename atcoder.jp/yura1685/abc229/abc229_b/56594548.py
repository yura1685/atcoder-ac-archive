a, b = map(str,input().split())
k = min(len(a),len(b))
for i in range(k):
    if int(a[-1-i])+int(b[-1-i]) >= 10:
        print('Hard')
        exit()
print('Easy')