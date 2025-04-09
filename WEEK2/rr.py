# #######################################2110###################################################################
# import sys

# n, c = map(int, sys.stdin.readline().split())
# home = []
# result = 0

# for i in range(n):
#     home.append(int(input()))

# home.sort()

# low = 1
# high = home[-1] - home[0]

# result = 0

# while low <= high:

#     installed = 1
#     last_installed = home[0]

#     mid = (low + high) // 2

#     for i in range(1, n):
#         if home[i] - last_installed >= mid:
#             installed += 1
#             last_installed = home[i]

#     if installed >= c:
#         result = mid
#         low = mid + 1
#     else:
#         high = mid - 1

# print(result)
# ###############################################################################################################

# #############################################2470###############################################################
# import sys

# N = int(sys.stdin.readline())
# liquid = list(map(int, sys.stdin.readline().split()))
# liquid.sort()

# left = 0
# right = N - 1
# sumLiquid = liquid[left] + liquid[right]
# resultLeft = 0
# resultRight = N - 1

# while left < right:

#     newSumLiquid = liquid[left] + liquid[right]

#     if newSumLiquid == 0:

#         resultLeft = left
#         resultRight = right
#         break

#     if abs(newSumLiquid) < abs(sumLiquid):
#         sumLiquid = newSumLiquid
#         resultLeft = left
#         resultRight = right

#     if newSumLiquid < 0:
#         left += 1
#     elif newSumLiquid > 0:
#         right -= 1

# print(liquid[resultLeft], liquid[resultRight])
# ###############################################################################################################

# # ############################################11053##############################################################
# import sys

# N = int(sys.stdin.readline())
# A = list(map(int, sys.stdin.readline().split()))

# a = [1] * N  # index 보다 앞에 작은 수 순서 개수?
# for i in range(N):
#     for j in range(i):
#         if A[j] < A[i]:
#             a[i] = max(a[i], a[j] + 1)

# print(max(a))
# #################################################################################################################

# ###################################################8983##########################################################
# import sys

# M, N, L = map(int, sys.stdin.readline().split())
# postionP = list(map(int, sys.stdin.readline().split()))
# animal = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

# postionP.sort()


# def binarySearch(a):
#     start, end = 0, M - 1
#     while start < end:
#         mid = (start + end) // 2
#         if postionP[mid] < a:
#             start = mid + 1
#         elif postionP[mid] == a:
#             return mid
#         else:
#             end = mid
#     return start


# count = 0

# for x, y in animal:
#     hunter = binarySearch(x)
#     if abs(x - postionP[hunter]) + abs(y) <= L:
#         count += 1
#     else:
#         if abs(x - postionP[hunter - 1]) + abs(y) <= L:
#             count += 1

# print(count)
# ###################################################8983##########################################################

# #################################################################################################################
# # N = int(input())
# # A = list(map(int, input().split()))


# # def LIS():
# #     if N == 0:
# #         return 0
# #     L = 0
# #     M = [0] * (N + 1)
# #     for i in range(N):
# #         l, h = 1, L
# #         while l <= h:
# #             mid = (l + h) // 2
# #             if A[M[mid]] < A[i]:
# #                 l = mid + 1
# #             else:
# #                 h = mid - 1
# #         new_L = l
# #         M[new_L] = i
# #         L = max([L, new_L])
# #     return L


# # print(LIS())
# ##################################################################################################

# ##################################################################################################
# N = int(input())
# A = list(map(int, input().split()))


# def LIS():
#     if N == 0:
#         return 0
#     L = 0
#     M = [0] * (N + 1)
#     for i in range(N):
#         l, h = 1, L
#         while l <= h:
#             mid = (l + h) // 2
#             if A[M[mid]] < A[i]:
#                 l = mid + 1
#             else:
#                 h = mid - 1
#         new_L = l
#         M[new_L] = i
#         L = max([L, new_L])
#     return L


# print(LIS())
