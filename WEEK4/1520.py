import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
M, N = map(int, input().split())
graph = []
direction = [(1,0),(-1,0),(0,1),(0,-1)]

for _ in range(M):
    graph.append(list(map(int, input().split())))

dp = [[-1]*N for _ in range(M)]
def dfs(x, y):
    
    if x == M-1 and y == N-1:
        return 1  # 목적지 도달

    if dp[x][y] != -1:
        return dp[x][y]  # 이미 계산된 경로 수 반환

    dp[x][y] = 0
    for dx, dy in direction:
        nx, ny = x + dx, y + dy
        if 0 <= nx < M and 0 <= ny < N:
            if graph[x][y] > graph[nx][ny]:
                dp[x][y] += dfs(nx, ny)
                
    
    return dp[x][y]

print(dfs(0, 0))
