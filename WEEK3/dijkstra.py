import heapq

def dijkstra(graph, start):
    
    distances = {node : float('inf') for node in graph} #딕셔너리 형태로 보관
    # 여기에 결과값을 저장할 거임

    distances[start] = 0  # 시작점

    priority_queue = [(0, start)] # 다음 최소값으로 가서 거서 찾아봐야하니까

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue) # 현재 노드의 값

        if current_distance > distances[current_node]:
            continue # 현재 노드의 값이 저장되있는 값보다 크면 의미없음

        # 이제 현재 노드부터 연결되있는 노드의 거리를 갱신해줘야함
        for neighbor, weight in graph[current_node].items(): # .item()이 각 값 꺼내기?
                distance = current_distance + weight

                if distance < distances[neighbor]: # 계산값과 저장된값 비교
                     #작다면 갱신 해줘야겠지?
                    distances[neighbor] = distance

                     # 갱신 했으니까 큐에 넣어주기
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
