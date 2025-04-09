import sys
import heapq

N = int(sys.stdin.readline())

hq = []

for i in range(N):
    heapq.heappush(hq, int(sys.stdin.readline()))

result = 0



while len(hq) > 1:
    
    a = heapq.heappop(hq)
    b = heapq.heappop(hq)
    count = a + b
    result = result + count
    heapq.heappush(hq, count)


print(result)

