import sys

input = sys.stdin.readline
import heapq

n = int(input())
maze = []

for i in range(n):
    maze.append(list(map(int, input().strip())))

# print(maze)
Direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def mazeRunner():
    visited = [[False for _ in range(n)] for i in range(n)]
    queue = [(0, 0, 0)]  # (벽 부순 개수, x좌표, y좌표)
    visited[0][0] = True

    while queue:
        k, a, b = heapq.heappop(queue)
        if a == n - 1 and b == n - 1:
            return k
        for x, y in Direction:
            if 0 <= a + x < n and 0 <= b + y < n:
                if not visited[a + x][b + y]:
                    if maze[a + x][b + y] == 1:
                        heapq.heappush(queue, (k, a + x, b + y))
                        visited[a + x][b + y] = True

                    elif maze[a + x][b + y] == 0:
                        heapq.heappush(queue, (k + 1, a + x, b + y))
                        visited[a + x][b + y] = True


print(mazeRunner())
