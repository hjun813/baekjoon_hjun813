import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())

road = {i: [] for i in range(1, n + 1)}
goback = {i: [] for i in range(1, n + 1)}
indegree = [0] * (n + 1)
nodeMaxCost = [0] * (n + 1)
queue = deque()

for _ in range(m):
    start, end, weight = map(int, input().split())
    road[start].append((end, weight))
    goback[end].append((start, weight))
    indegree[end] += 1

start_city, end_city = map(int, input().split())

for i in range(1, n + 1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    k = queue.popleft()
    for next, cost in road[k]:
        nodeMaxCost[next] = max(nodeMaxCost[next], nodeMaxCost[k] + cost)
        indegree[next] -= 1
        if indegree[next] == 0:
            queue.append(next)

maxTime = nodeMaxCost[end_city]
print(maxTime)

queue.append(end_city)
result = set()
visited = set()
while queue:
    k = queue.popleft()
    for next, cost in goback[k]:
        if nodeMaxCost[next] == nodeMaxCost[k] - cost:
            if (k, next) not in result:  # 중복 간선 방지
                result.add((k, next))
            if next not in visited:  # 중복 방문 방지
                queue.append(next)
                visited.add(next)

print(len(result))

