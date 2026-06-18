m = int(input())

if m < 100:
    vv = '00'
if 100 <= m <= 5000:
    vv = str(m//100)
    if len(vv) == 1:
        vv = '0' + vv
if 6000 <= m <= 30000:
    vv = m//1000 + 50
if 35000 <= m <= 70000:
    vv = (m//1000-30)//5 + 80
if 70000 < m:
    vv = 89

print(vv)