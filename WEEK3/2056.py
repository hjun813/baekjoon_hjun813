import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N, M, K = map(int, input().split())
visited = [False] * K
trash = []
amount = []
count = 0

for i in range(K):
    x, y = map(int, input().split())
    trash.append((x, y))

direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def dfs(n):
    x, y = trash[n]
    visited[n] = True
    global count
    count += 1
    for a, b in direction:
        if 0 <= a + x < N + 1 and 0 <= b + y < M + 1:
            for i in range(K):
                if not visited[i]:    
                    
                    if (a + x, b + y) == trash[i]:
                    
                        dfs(i)
                        visited[i] = True


for i in range(K):
    count = 0
    if not visited[i]:
        dfs(i)
        amount.append(count)

print(max(amount))
