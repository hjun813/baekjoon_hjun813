# ==================================================================================================
# import sys
# N, C = map(int, sys.stdin.readline().split())
# home = []

# for _ in range(N):
#     home.append(int(sys.stdin.readline()))
# home.sort()

# # 간격을 이분탐색하여 최적의 거리 찾기!
# low = 1
# high = home[-1]

# answer = 0

# while low <= high:

#     mid = (low + high) // 2
#     installed = 1
#     last_installed = home[0]

#     for i in range(1,N):
#         if home[i] - last_installed >= mid:
#             installed += 1
#             last_installed = home[i]

#     if installed >= C:
#         answer = mid
#         low = mid +1

#     elif installed < C:
#         high = mid -1

# print(answer)

# ==================================================================================================


# ==================================================================================================
# import sys

# N = int(sys.stdin.readline())
# liquidList = list(map(int, sys.stdin.readline().split()))
# liquidList.sort()

# left = 0
# right = N - 1

# finalLeft = 0
# finalRight = N - 1
# beforeSum = liquidList[left] + liquidList[right]

# while left < right:


#     sumLiquid = liquidList[left] + liquidList[right]

#     if sumLiquid == 0:
#         finalLeft = left
#         finalRight = right
#         break

#     if abs(beforeSum) > abs(sumLiquid):
#         finalLeft = left
#         finalRight = right
#         beforeSum = sumLiquid

#     if sumLiquid < 0:
#         left += 1
        
#     elif sumLiquid > 0:
#         right -= 1

# print(liquidList[finalLeft], liquidList[finalRight])

#==========================================================================================================

#==========================================================================================================
