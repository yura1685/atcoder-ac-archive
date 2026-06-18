sx, sy, tx, ty = map(int,input().split())

tx -= sx
ty -= sy

ans = ''
ans += 'R'*tx + 'U'*ty + 'L'*tx + 'D'*(ty+1)
ans += 'R'*(tx+1) + 'U'*(ty+1) + 'L' + 'U' 
ans += 'L'*(tx+1) + 'D'*(ty+1) + 'R'
print(ans)