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

circle.sort(key=lambda x: (x[0], -(x[1])))
for i in range(N):
    dq.append(circle[i])
print("dq", dq)
count = 1

