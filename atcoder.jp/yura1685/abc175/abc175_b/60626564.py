N = int(input())
L = sorted(list(map(int,input().split())))
ans = 0
if N <= 2:
  print(ans)
  exit()
for i in range(N-2):
  for j in range(i+1,N-1):
    for k in range(j+1,N):
      if L[i] + L[j] > L[k]:
        if len(set([L[i],L[j],L[k]])) == 3:
            ans += 1
      else:
        break
print(ans)