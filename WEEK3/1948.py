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


# print(road)
# print(indegree)
# print(queue)


while queue:
    k = queue.popleft()
    for next, cost in road[k]:
        nodeMaxCost[next] = max(nodeMaxCost[next], nodeMaxCost[k] + cost)
        indegree[next] -= 1
        if indegree[next] == 0:
            queue.append(next)

# print(nodeMaxCost)
maxTime = nodeMaxCost[end_city]
print(maxTime)
# print(goback)

count = 0
queue.append(end_city)
result = []
while queue:
    k = queue.popleft()
    for next, cost in goback[k]:
        if nodeMaxCost[next] == nodeMaxCost[k] - cost:
            count += 1
            # print('!!',k, next)
            result.append((k,next))
            # outdegree[next] -= 1
            # if outdegree[next] == 0:
            queue.append(next)

# print("count", count)
print(len(set(result)))

