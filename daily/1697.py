import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
answer = 0
queue = []
visited = [0 for _ in range(100001)]
heapq.heappush(queue, (0, N)) # (시간, 위치)
visited[N] = 1

while queue:
    time, pos = heapq.heappop(queue)

    if pos == K:
        answer = time
        break
    if 0<=pos-1<= 100000 and not visited[pos-1]:
        visited[pos-1] = 1
        heapq.heappush(queue, (time+1, pos-1))
        
    if 0<=pos+1<= 100000 and not visited[pos+1]:
        visited[pos+1] = 1
        heapq.heappush(queue, (time+1, pos+1))

    if 0<=pos*2<= 100000 and not visited[pos*2]:
        visited[pos*2] = 1
        heapq.heappush(queue, (time+1, pos*2))
        
print(answer)