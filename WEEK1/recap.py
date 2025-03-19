# ====================================================================================================================
# 9663 N-Queen
# num = int(input())
# nQueenPos = [0] * num
# nQueenPosHor = [False] * num
# nQueenPostive = [False] * (num * 2 - 1)
# nQueenNegative = [False] * (num * 2 - 1)
# count = 0


# def nQueen(num, n):
#     global count
#     if n < num:

#         for i in range(num):

#             if not nQueenPosHor[i] and not nQueenPostive[n + i] and not nQueenNegative[n - i + num - 1]:
#                 nQueenPos[n] = i

#                 nQueenPosHor[i] = True
#                 nQueenPostive[n + i] = True
#                 nQueenNegative[n - i + num - 1] = True
#                 nQueen(num, n + 1)
#                 nQueenPosHor[i] = False
#                 nQueenPostive[n + i] = False
#                 nQueenNegative[n - i + num - 1] = False

#     elif n == num:
#         # print(nQueenPos)
#         count = count+1


# nQueen(num, 0)
# print(count)
# ====================================================================================================================

# ====================================================================================================================
# 10819 차이를 최대로~
# N = int(input())
# arr = list(map(int, input().split()))
# orderedArr = [0] * N
# used = [False] * N
# between = [0] * (N-1)
# betweenList = []
# maxBetween = 0

# def orderArr(arr, n):
#     if n < N:
#         for i in range(N):
#             if not used[i]:
#                 orderedArr[n] = arr[i]
#                 used[i] = True
#                 orderArr(arr, n + 1)
#                 used[i] = False
#     elif n == N:
#         # print(orderedArr)
#         for i in range(len(orderedArr)-1):
#             if orderedArr[i] - orderedArr[i+1] < 0:
#                 between[i] = -(orderedArr[i] - orderedArr[i+1])
#             else:
#                 between[i] = orderedArr[i] - orderedArr[i+1]
#         betweenList.append(sum(between))


# orderArr(arr, 0)
# print(max(betweenList))
# ====================================================================================================================

# ====================================================================================================================
# 10971 외판원 순회
import sys

N = int(input())
rows = N
cols = N
cost = [[0 for j in range(cols)] for i in range(rows)]
visited = [False] * N
minCost = float("inf")

for i in range(N):
    cost[i] = list(map(int, sys.stdin.readline().rstrip().split()))


def tripTo(depth, now, nowCost, start):
    global minCost

    if nowCost >= minCost:
        return

    if depth == N - 1:
        if cost[now][start] > 0:
            minCost = min(minCost, nowCost + cost[now][start])
        return

    for i in range(N):
        if not visited[i] and cost[now][i] > 0:
            visited[i] = True
            tripTo(depth + 1, i, nowCost + cost[now][i], start)
            visited[i] = False

visited[0]=True
tripTo(0, 0, 0, 0)
visited[0]=False

print(minCost)
# ====================================================================================================================

# ====================================================================================================================
# # 2468 안전 영역 - 더 공부해볼것
# import sys

# num = int(input())
# rows = num
# cols = num
# heightInfo = [[0 for j in range(rows)] for i in range(cols)]
# drowning = [[False for j in range(rows + 2)] for i in range(cols + 2)]
# checking = [[False for j in range(rows + 2)] for i in range(cols + 2)]
# count = 0
# islandNum =[]

# for i in range(num + 2):
#     drowning[0][i] = True
# for i in range(num + 2):
#     drowning[num + 1][i] = True
# for i in range(num + 2):
#     drowning[i][0] = True
#     drowning[i][num + 1] = True

# for i in range(num + 2):
#     checking[0][i] = True
# for i in range(num + 2):
#     checking[num + 1][i] = True
# for i in range(num + 2):
#     checking[i][0] = True
#     checking[i][num + 1] = True

# maxRainList = []
# maxRain = 0
# minRainList = []
# minRain = 0


# for i in range(num):
#     heightInfo[i] = list(map(int, sys.stdin.readline().rstrip().split()))

# for i in range(num):
#     maxRainList.append(max(heightInfo[i]))
# maxRain = max(maxRainList)
# for i in range(num):
#     minRainList.append(min(heightInfo[i]))
# minRain = min(minRainList)

# # for i in range(num+2):
# #     print(drowning[i])


# def raining(arr):
#     for i in range(minRain, maxRain):
#         print("Raining : ", i)
#         for j in range(num):
#             for v in range(num):
#                 if arr[j][v] - i <= 0:
#                     drowning[j + 1][v + 1] = True

                
#         for j in range(num + 2):
#             print("Drowning", drowning[j])
        
#         for j in range(num):
#             for v in range(num):
                
#                 findIsland(drowning, j+1, v+1)
#                 print()
#                 for k in range(num + 2):
                    
#                     print("checking", checking[k])
                

#         print()

       

        


#         print("===================================")


# def findIsland(arr, i, j):


#     if not checking[i][j]:
#         if not arr[i][j]:
            
#             checking[i][j] = True
#             if not arr[i][j + 1]:  # 우
#                 if not checking[i][j + 1]:
#                     return findIsland(arr, i, j + 1)
#             if not arr[i + 1][j]:  # 하
#                 if not checking[i + 1][j]:
#                     return findIsland(arr, i + 1, j)
#             if not arr[i][j - 1]:  # 좌
#                 if not checking[i][j - 1]:
#                     return findIsland(arr, i, j - 1)
#             if not arr[i - 1][j]:  # 상
#                 if not checking[i - 1][j]:
#                     return findIsland(arr, i - 1, j)


# raining(heightInfo)


# ====================================================================================================================
# 2798
# from itertools import combinations


# n, m = map(int, input().split())

# cardInfo = list(map(int, input().split()))
# ans = 0



# for i in combinations(cardInfo, 3):
#     total = sum(i)
#     if total <= m and total > ans:
#         ans = total       

# print(ans)
# ====================================================================================================================

# ====================================================================================================================