import sys
from collections import deque

N = int(sys.stdin.readline())
circle = []
dq = deque(circle)
circleDiv = []


for _ in range(N):
    x, r = map(int, sys.stdin.readline().split())
    start, end = x-r, x+r
    circle.append([start, end])    

circle.sort(key=lambda x: (x[0], -(x[1]-x[0])))
for i in range(N):
    dq.append(circle[i])
print("dq", dq)
count = 1

# while True:

#     next = dq.popleft()
#     print("!!dq",dq)
#     print("next", next)
#     print("!!circleDiv",circleDiv)

#     if len(circleDiv) == 0:
#         circleDiv.append(next)
#     else:
#         if circleDiv[-1][0] != next[0] :#시작점 다르면
#             circleDiv.pop()
#             if circleDiv[-1][1] == next[0]:
#                 if circleDiv[-2][1] == next[1]:
#                     #1개 더 추가

#             circleDiv.pop()
#             circleDiv.append(next)
#         else : # 시작점 같을 때
#             circleDiv.append(next)






