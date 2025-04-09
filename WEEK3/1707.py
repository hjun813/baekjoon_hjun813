import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
K = int(input())


def dfs(g, v, visited, check):
    visited[v] = check
    # 출력이나 추가
    for i in g[v]:
        if visited[i] == 0:
            dfs(g, i, visited, -check)
        elif visited[i] == check:
            visited[0] = 4

for _ in range(K):
    V, E = map(int, input().split())
    graph = {i : [] for i in range(1, V+1)}
    visited = [0] * (V+1)
    for i in range(E):
        node1, node2 = map(int, input().split())
        graph[node1].append(node2)
        graph[node2].append(node1)

    for i in graph:
        graph[i].sort()
    
    print(graph)

    for i in range(1, V + 1):
        if visited[i] == 0:  # 아직 방문하지 않은 경우
            dfs(graph, i, visited, 1)

    

    # print(visited)
    if visited[0] == 4:
        print("NO")
    else:
        print("YES")
    

    