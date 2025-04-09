# TSP (traveling Salesman problem)

# 각 도시를 방문했는지의 여부는 비트마스킹을 활용하고
# 현재 도시에서의 최소비용은 DP를 활용하고
# 도시를 방문하는 것은 DFS를 활용한다.

# 점화식 : 
# dp[cur][visited] = min(dp[cur][visited], dp[next][visited | (1 << next)] + graph[cur][next])

n = int(input())

INF = int(1e9)
dp = [[INF] * (1 << n) for _ in range(n)] # 1 << n 은 2**n 을 의미함 

def dfs(x, visited):
    if visited == (1 << n) - 1:     # 모든 도시를 방문했다면
        if graph[x][0]:             # 출발점으로 가는 경로가 있을 때
            return graph[x][0]
        else:                       # 출발점으로 가는 경로가 없을 때
            return INF

    if dp[x][visited] != INF:       # 이미 최소비용이 계산되어 있다면
        return dp[x][visited]

    for i in range(1, n):           # 모든 도시를 탐방
        if not graph[x][i]:         # 가는 경로가 없다면 skip
            continue
        if visited & (1 << i):      # 이미 방문한 도시라면 skip 
            continue                # (1<<i) 가 2**i 이니까 100000 이런식임 i+1번째만 1

        # 점화식 부분(위 설명 참고)
        dp[x][visited] = min(dp[x][visited], dfs(i, visited | (1 << i)) + graph[x][i])
    return dp[x][visited]


graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

print(dfs(0, 1))