import heapq

class MinHeap:
    def __init__(self):
        self._heap = []
    def push(self, item):
        heapq.heappush(self._heap, item)
    def pop(self):
        return heapq.heappop(self._heap)
    def __len__(self):
        return len(self._heap)
    
N, M = map(int, input().split())
hq = MinHeap()
for _ in range(N):
    F, D = map(int, input().split())
    hq.push((-F, D))

ans = 0
for _ in range(M):
    if not hq:
        break
    f, d = hq.pop()
    f = -f
    ans += f
    f -= d
    if f > 0:
        hq.push((-f, d))
print(ans)