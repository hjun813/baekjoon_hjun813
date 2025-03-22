import heapq
import sys

N = int(sys.stdin.readline())
x =[]

for i in range(N):
    x.append(int(sys.stdin.readline()))

heap =[]
# print()
for i in range(N):
    if x[i] != 0:
        heapq.heappush(heap, -x[i])
        # print("heap:", heap)
    elif x[i] == 0:
        if len(heap) == 0:
            print(0)
        else:
            # print("heap:", heap)
            print(-heap[0])
            heapq.heappop(heap)
            # print("heap pop:", heap)