A, B = map(int,input().split())
plug = 1
use = 0
while plug < B:
    plug += -1 + A
    use += 1
print(use)