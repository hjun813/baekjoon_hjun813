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
    '1': {'2': 2, '3': 3,'4': 1,'5': 10},
    '2': {'4': 2},
    '3': {'4': 1, '5': 1},
    '4': {'5': 3},
    '5': {}
    
}

print(dijkstra(graph, '1'))
