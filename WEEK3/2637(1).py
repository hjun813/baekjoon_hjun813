import sys
from collections import deque

input = sys.stdin.readline

# 입력 받기
N = int(input())  # 1~N-1은 부품, N은 완제품
M = int(input())

# 그래프 및 진입 차수 초기화
graph = {i: [] for i in range(1, N+1)}
indegree = [0] * (N + 1)

# 부품 조합 정보 저장
for _ in range(M):
    X, Y, K = map(int, input().split())
    graph[Y].append((X, K))  # X를 조립하려면 Y가 K개 필요
    indegree[X] += 1  # X의 진입 차수 증가
print()
print(graph)
print(indegree)
print()
# 기본 부품 리스트 및 DP 테이블 (필요 개수 저장)
basic_parts = []
needed = [[0] * (N + 1) for _ in range(N + 1)]  # needed[i][j]: i를 만들 때 j가 몇 개 필요한지

# 위상 정렬 (BFS)
queue = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:  # 기본 부품==
        queue.append(i)
        basic_parts.append(i)

# 그럼 queue에 기본부품만 들어 있겠네 
while queue:
    print(queue)
    part = queue.popleft()
    
    for next_part, count in graph[part]:
        # 기본 부품이면 바로 추가
        if part in basic_parts:
            needed[next_part][part] += count
        else:
            for i in range(1, N + 1):
                needed[next_part][i] += needed[part][i] * count
        
        # 진입 차수 감소 후 0이면 큐에 추가
        indegree[next_part] -= 1
        if indegree[next_part] == 0:
            queue.append(next_part)

# 결과 출력 (N을 만들 때 필요한 기본 부품 개수)
for part in basic_parts:
    print(part, needed[N][part])


