import sys
from collections import deque

N = int(sys.stdin.readline())

testData = []


for i in range(N):
    testData.append(list(map(str, sys.stdin.readline())))

q = deque(testData)
right = 0
left = 0

for i in range(N):
    q[i].pop()
    right = 0
    left = 0

    for j in range(len(q[i])):

        if q[i][j] == "(":
            # print("hi")
            left += 1
        elif q[i][j] == ")":
            # print("hello")
            right += 1

        if right > left:
            print("NO")
            
            break

        # q[i].popleft()
    
    if left == right :
        # print(left, right)
        print("YES")
    elif right>left:
        continue
    else:
        # print(left, right)
        print("NO")
        
