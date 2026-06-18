#入力の受取とグリッドの作成
H, W = map(int,input().split())
glid = ['.'*(W+2)]
for i in range(H):
    S = '.' + input() + '.'
    glid.append(S)
glid.append('.'*(W+2))

#座標管理リスト
check_s = []
for h in range(1,H+1):
    for w in range(1,W+1):
        if glid[h][w] == 's':
            check_s.append([(h,w)]) #sの座標 [(h,w)] を追加

check_sn = []

for s in check_s:
    h, w = s[0]
    if glid[h-1][w-1] == 'n':
        check_sn.append([(-1,-1),(h,w)]) #snの続く方向を記録
    if glid[h-1][w] == 'n':
        check_sn.append([(-1,0),(h,w)])
    if glid[h-1][w+1] == 'n':
        check_sn.append([(-1,1),(h,w)])
    if glid[h][w-1] == 'n':
        check_sn.append([(0,-1),(h,w)])
    if glid[h][w+1] == 'n':
        check_sn.append([(0,1),(h,w)])
    if glid[h+1][w-1] == 'n':
        check_sn.append([(1,-1),(h,w)])
    if glid[h+1][w] == 'n':
        check_sn.append([(1,0),(h,w)])
    if glid[h+1][w+1] == 'n':
        check_sn.append([(1,1),(h,w)])

for lastcheck in check_sn:
    del_h, del_w = lastcheck[0]
    ans = []
    h, w = lastcheck[1]
    snuke = 'snuke'
    for i in range(5): #5文字一致するか検証。違う文字か枠に触れたらアウト
        if glid[h][w] == snuke[i]:
            ans.append((h,w))
            h += del_h
            w += del_w
        else:
            break
    if len(ans) == 5:
        break

for i in ans:
    print(i[0],i[1])