# import sys
# num = int(input())
# rows = num
# cols = num
# cost = [[0 for j in range(cols)] for i in range(rows)]
# travel = [False] * num  # 방문한 나라 여부 확인
# trip = [0] * num  # 방문한 나라 인덱스 저장
# totalCostAll = []


# for i in range(num):
#     cost[i] = list(map(int, sys.stdin.readline().rstrip().split()))


# # def printTrip(N):

# #     calculateCost(trip)


# def calculateCost(arr):
#     total = 0
#     totalList = []

#     for i in range(len(arr)):
#         if i == len(arr) - 1:
#             totalList.append(int(cost[arr[i]][arr[0]]))
#             total += cost[arr[i]][arr[0]]

#         else:

#             totalList.append(int(cost[arr[i]][arr[i + 1]]))
#             total += cost[arr[i]][arr[i + 1]]

#     if totalList.count(0) == 0:
#         totalCostAll.append(total)


# def travelTo(a, n, N, nowCost):
#     global minCost
#     if nowCost >= minCost:
#         return
#     for i in range(N):
#         if not travel[i]:
#             trip[n] = i
#             if n == N - 1:
#                 calculateCost(trip)
#             else:
#                 travel[i] = True
#                 travelTo(a + i, n + 1, N, )
#                 travel[i] = False


# travelTo(0, 0, num, 0)

# print(min(totalCostAll))


import sys

num = int(input())
cost = [list(map(int, sys.stdin.readline().split())) for _ in range(num)]
visited = [False] * num
min_cost = float('inf')

def dfs(depth, current, total_cost, start):
    global min_cost

    # 현재 비용이 기존 최소 비용보다 크면 탐색 종료 (가지치기)
    if total_cost >= min_cost:
        return

    # 모든 도시 방문 완료
    if depth == num - 1:
        if cost[current][start] > 0:  # 시작점으로 돌아갈 수 있는 경우만 고려
            min_cost = min(min_cost, total_cost + cost[current][start])
        return

    # 다음 도시 방문
    for next_city in range(num):
        if not visited[next_city] and cost[current][next_city] > 0:
            visited[next_city] = True
            dfs(depth + 1, next_city, total_cost + cost[current][next_city], start)
            visited[next_city] = False

# 첫 번째 도시부터 탐색 시작
for start in range(num):
    
    visited[start] = True
    dfs(0, start, 0, start)
    visited[start] = False


# 걍 어느 도시에서든지 출발해도 같음
# visited[0] = True
# dfs(0, 0, 0, 0)
# visited[0] = False

print(min_cost)
