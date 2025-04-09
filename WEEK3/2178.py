import sys

input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())
maze = []

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for _ in range(N):
    maze.append(list(map(int, input().strip())))

print(maze)

def bfs():
    queue = deque([(0, 0)])
    while queue:
        print(queue)
        a, b = queue.popleft()
        for i in range(4):
            na, nb = a + direction[i][0], b + direction[i][1]
            if 0 <= na < N and 0 <= nb < M:
                if maze[na][nb] == 1:
                    queue.append((na, nb))
                    maze[na][nb] = maze[a][b] + 1

bfs()

print()
for i in range(N):
    print(maze[i])
    
print(maze[-1][-1])