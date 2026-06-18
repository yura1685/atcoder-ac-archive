N = int(input())
A = list(map(int,input().split()))

Even = []
Odd = []
for i in A:
    if i % 2 == 0:
        Even.append(i)
    else:
        Odd.append(i)

if len(Even) <= 1 and len(Odd) <= 1:
    print(-1)
    exit()

even, odd = 0, 0
if len(Even) > 1:
 even = max(Even)
 Even.remove(even)
 even += max(Even)


if len(Odd) > 1:
 odd = max(Odd)
 Odd.remove(odd)
 odd += max(Odd)

print(max(even,odd))