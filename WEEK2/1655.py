import sys

# 직관적으로 이해하기는 어렵지만
# 중앙값과 중앙값보다 작은 숫자는 max 힙으로 보관
# 큰 숫자는 min 힙으로 보관
# 이러면 max힙 루트는 중앙값, min힙 루트는 중앙값 바로 다음
# min 힙 개수가 max 힙 개수 보다 많아지면 중앙값이 바뀌기 때문에 min 루트 max로
# max 도 min보다 1개 까지는 괜찮은데 2개부터 중앙값이 바뀌어서 max 루트 min으로

# from collections import deque
import heapq

N = int(sys.stdin.readline())
maxHq = []
minHq = []


mid = int(sys.stdin.readline())
heapq.heappush(maxHq, (-mid))
print("ans",mid)

for i in range(1, N):
    
    k = int(sys.stdin.readline())

    if (-maxHq[0]) > k:
        heapq.heappush(maxHq, -k)
    elif (-maxHq[0]) <= k:
        heapq.heappush(minHq, k)
        if len(minHq)> len(maxHq):
            v = heapq.heappop(minHq)
            heapq.heappush(maxHq, -v)


    if len(maxHq) - len(minHq) >= 2:
        v = heapq.heappop(maxHq)
        heapq.heappush(minHq, -v)

    elif len(minHq) - len(maxHq) >= 2:
        v = heapq.heappop(minHq)
        heapq.heappush(maxHq, -v)

    print("maxHq",maxHq, "minHq",minHq)
    print("ans", (- maxHq[0]))
