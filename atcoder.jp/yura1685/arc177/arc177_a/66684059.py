coin = list(map(int,input().split()))
N = int(input())
X = list(map(int,input().split()))
d = {5:1, 4:5, 3:10, 2:50, 1:100, 0:500}

def pay(n):
    for i in range(6):
        while n >= d[i] and coin[5-i] > 0:
            n -= d[i]
            coin[5-i] -= 1
    if n == 0:
        return True
    else:
        return False
    
c = [pay(x) for x in X]

print('Yes' if all(c) else 'No')