# import sys

# n, m = map(int, sys.stdin.readline().split())

# height = list(map(int, sys.stdin.readline().split()))
# height.sort()
# maxHeight = height[n - 1]
# get = 0


# def findTreeIndex(cut, height, start, end):
#     if start < end:
#         mid = int((start + end) // 2)

#         if height[mid] == cut:
#             return mid + 1
#         elif height[mid] < cut:
#             return findTreeIndex(cut, height, mid + 1, end)
#         else:
#             return findTreeIndex(cut, height, start, mid - 1)
#     elif start == end:
#         if height[start] == cut:
#             return start + 1
#         elif height[start] < cut:
#             return start + 1
#         else:
#             return start - 1
#     else:
#         return start


# def cutTree(min, max):

#     global get

#     midHeight = (min + max) // 2

#     checkFrom = findTreeIndex(midHeight, height, 0, n - 1)

#     for i in range(checkFrom, n):
#         # print("!", get, height[i], midHeight)
#         if (height[i] - midHeight) > 0:
#             get = get + height[i] - midHeight

#     if max - min != 1 and max - min != 0:

#         # print(get, m, midHeight)
#         if get == m:
#             return midHeight
#         elif get > m:
#             get = 0
#             return cutTree(midHeight, max)
#         elif get < m:
#             get = 0
#             return cutTree(min, midHeight)
#     else:
#         return midHeight

# if n==1 :
#     print(height[0]-m)
# else:
#     print(cutTree(0, maxHeight))

import sys

n, m = map(int, sys.stdin.readline().split())
height = list(map(int, sys.stdin.readline().split()))
height.sort()
maxHeight = height[n - 1]
get = 0

def binarySearch(n, start, end):
    global get

    if start > end:
        return None

    mid = (start + end) // 2

    for i in range(n):
        if height[i] > mid:
            get = get + height[i] - mid

    # print("get ", get, " m ", m, " start ", start," mid ", mid, " end ", end)

    if get < m:
        if start == end:
            return start - 1
        get = 0
        return binarySearch(n, start, mid - 1)
    
    elif get > m:
        if start == end:
            return start
        get = 0
        return binarySearch(n, mid + 1, end)
    elif get == m:
        return mid


print(binarySearch(n, 0, maxHeight))

# 어차피 높이차를 생각하면 정렬된 리스트에서 찾는거랑 별반 다를바가 없다.
