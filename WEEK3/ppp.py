from collections import deque
# 위상정렬 - > 작업순서가 정해져 있을 때 순서를 결정해주기 위한 알고리즘
def topological_sort(n, edges):

    graph = {i: [] for i in range(n)} # 그래프 딕셔너리
    indegree = {i: 0 for i in range(n)} # 진입 차수 => 들어오는 노드 수

    # 그래프 구성 및 진입 차수 계산
    for u, v in edges:
        graph[u].append(v)
        graph[u].sort()
        indegree[v] += 1

    print(graph)
    print(indegree)
    # 진입 차수가 0인 노드 큐에 삽입
    queue = deque([node for node in indegree if indegree[node] == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        # 연결된 노드의 진입 차수 감소
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    # 그래프 내 모든 노드를 정렬하지 못하면 사이클 존재
    if len(result) != n:
        return "사이클이 존재하여 위상 정렬 불가능"

    return result

# 예제 사용
n = 6
edges = [(5, 2), (5, 0), (4, 0), (4, 1), (2, 3), (3, 1)]
print(topological_sort(n, edges))

#================================================================================
import heapq

def dijkstra(graph, start):

    distances = {node: float('inf') for node in graph}

    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance

                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


graph = {
    'A': {'B': 1, 'C': 2},
    'B': {'A': 1, 'E': 2, 'D': 6},
    'C': {'A': 2, 'E': 3, 'F': 8},
    'D': {'B': 6, 'E': 1},
    'E': {'B': 2, 'C': 3, 'D': 1, 'F': 7},
    'F': {'C': 8, 'E': 7}
}

print(dijkstra(graph, 'A'))

# # #=============================================================================
import sys

input = sys.stdin.readline

n = int(input())
v = int(input())
INF = 999999
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(v):
    v1, v2, c = map(int, input().split())
    graph[v1][v2] = c #방향성 있는 그래프 인접 행렬

for i in range(1, n+1):
    graph[i][i] = 0 # 자기쪽으로 갈수 없으니까

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print("0", end=" ")
        else:
            print(graph[i][j], end=" ")
    print()
