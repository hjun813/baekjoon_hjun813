# # TSP (traveling Salesman problem)

# import sys
# input = sys.stdin.readline

# N = int(input())

# mapInfo = []

# for _ in range(N):
#     mapInfo.append(list(map(int, input().split())))

# print(mapInfo)

# dp = [[-1] * N for _ in range(1 << N)] # 비트 마스킹?

# INF = float('inf')

# def tsp(visited, current):
#     if visited == (1<<N) - 1:
#         return mapInfo[current][0] if mapInfo[current][0] els