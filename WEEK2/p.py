# import sys


# def function1(arr):

#     maxSquare = 0
#     check = [[-1, -1]]

#     for i in range(len(arr)):
#         if arr[i] > check[-1][1]:
#             check.append([i, arr[i]])
#         else:
#             while check[-1][1] >= arr[i]:

#                 [idx, h] = check.pop()
#                 tmp = (i - idx) * h
#                 maxSquare = max(maxSquare, tmp)
#             check.append([idx, arr[i]])

#     # print(maxSquare)
#     # print(check)

#     while check:
#         i, h = check.pop()
#         w = n - i
#         # print(h * w)
#         maxSquare = max(maxSquare, h * w)


#     return maxSquare


# while True:
#     recInfo = list(map(int, sys.stdin.readline().split()))
#     if len(recInfo) == 1:
#         break
#     n = recInfo[0]
#     recHeight = recInfo[1 : len(recInfo)]

#     print(function1(recHeight))


import sys

n = int(sys.stdin.readline())
circle_info = []
stack = []
count = 1

for i in range(n):
    r, c = list(map(int, sys.stdin.readline().split()))
    circle_info.append([r - c, "("])
    circle_info.append([r + c, ")"])

circle_info.sort(key=lambda x: (x[0], -ord(x[1])))

for i in range(n * 2):

    if stack:
        if circle_info[i][1] == "(" and circle_info[i][0] == stack[-1]["pos"]:

            stack[-1]["state"] = 2

        elif circle_info[i][1] == ")":
            count += stack.pop()["state"]

            if not stack:
                continue

            if i + 1 < 2 * n and circle_info[i + 1][0] != circle_info[i][0]:
                stack[-1]["state"] = 1
            continue

    stack.append({"pos": circle_info[i][0], "shape": circle_info[i][1], "state": 1})

print(count)

######################################################################################

import sys
import heapq

n = int(sys.stdin.readline())
people = []

for _ in range(n):
    home, work = map(int, sys.stdin.readline().split())
    people.append((min(home, work), max(home, work)))

d = int(sys.stdin.readline())
people.sort(key=lambda x: x[1])


heap = []
max_count = 0


for home, work in people:

    start = work - d

    heapq.heappush(heap, home)

    while heap and heap[0] < start: # 힙이 비어있지 않고, 기차 시작점보다 작으면 계속 pop 하기
        heapq.heappop(heap)

    max_count = max(max_count, len(heap))


print(max_count)
