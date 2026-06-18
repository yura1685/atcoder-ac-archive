N = int(input())
S = [input() for _ in range(N)]
T = list(zip(*S))

def f(n):
    db = []
    for t in T:
        db.append(t.count(str(n)))
    slot = 0
    while sum(db) != 0:
        if db[slot%10] != 0:
            db[slot%10] -= 1
        slot += 1
    return slot-1

print(min([f(n) for n in range(10)]))