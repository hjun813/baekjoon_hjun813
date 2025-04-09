import sys
import heapq
input = sys.stdin.readline
N = int(input())
M = int(input())

graph = {node: [] for node in range(1, N + 1)}

for i in range(M):
    start, end, weight = map(int, input().split())
    graph[start].append([end, weight]) 
print(graph)

start_node, end_node = map(int, input().split())

def dijkstra(graph, start, end):

    distances = {node : float('inf') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        # print(distances)
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    
    return distances[end]

print(dijkstra(graph, start_node, end_node))