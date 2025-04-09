# import sys

# M, N, L = map(int, sys.stdin.readline().split())

# postionP = list(map(int, sys.stdin.readline().split()))

# postionP.sort()
# animal = []
# for i in range(N):
#     animalX, animalY = map(int, sys.stdin.readline().split())
#     animal.append((animalX, animalY))

# animal.sort()
# # print(postionP)
# # print(animal)
# count = 0


# def binarySearch(a, start, end):
#     mid = (start + end) // 2
#     if start + 1 < end:
#         if postionP[mid] == a:
#             return mid
#         elif postionP[mid] < a:
#             return binarySearch(a, mid + 1, end)
#         elif postionP[mid] > a:
#             return binarySearch(a, start, mid - 1)
#     elif start == end:
#         return mid
#     elif start + 1 == end:
#         return start
#     return start


# for i in range(N):

#     k = postionP[binarySearch(animal[i][0], 0, M - 1)]
#     if len(postionP) != 1:
#         v = postionP[binarySearch(animal[i][0], 0, M - 1) + 1]
#     else:
#         v = postionP[binarySearch(animal[i][0], 0, M - 1)]
#     # print("i", i, "k", k)
#     # print("i", i, "v", v)

#     if ((abs(animal[i][0] - k)) + animal[i][1]) <= L:
#         # print(animal[i])
#         count += 1
#         continue
#     if ((abs(animal[i][0] - v)) + animal[i][1]) <= L:
#         # print(animal[i])
#         count += 1

# print(count)

#########################################################################################
import sys

# 입력 받기
M, N, L = map(int, sys.stdin.readline().split())
postionP = list(map(int, sys.stdin.readline().split()))
animal = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

# 사냥터 위치 정렬
postionP.sort()

# 이진 탐색 함수
def binarySearch(a):
    start, end = 0, M - 1
    while start < end:
        mid = (start + end) // 2
        if postionP[mid] < a:
            start = mid + 1
        else:
            end = mid
    return start

count = 0
for x, y in animal:
    idx = binarySearch(x)

    closest = postionP[idx]

    if idx > 0:  # 왼쪽 사냥터도 비교 가능하면 비교
        left = postionP[idx - 1]
        if abs(left - x) < abs(closest - x):
            closest = left

    if abs(closest - x) + y <= L:
        count += 1

print(count)
