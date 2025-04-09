import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
coinValue = []


for _ in range(n):
    coinValue.append(int(input()))

# print(coinValue)


def bfs():
    queue = deque([(0, 0)])
    visited = [False] * (k+1)
    while queue:
        
        current_value, current_coinN = queue.popleft()
        visited[current_value] = True
        
        for value in coinValue:
            next_value = current_value + value
            next_coinN = current_coinN + 1
        
            if next_value < k:
                if not visited[next_value]:
                    if (next_value,next_coinN) in queue:
                        continue
                    else:
                        visited[next_value] = True
                        queue.append((next_value, next_coinN))
            
            elif next_value == k:
                return next_coinN
            
            else:
                continue

    return -1

print(bfs())