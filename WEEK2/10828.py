import sys
from collections import deque

N = int(sys.stdin.readline())
info = [] 
a =[]
q = deque(a)



for i in range(N):
    info.append(list(map(str, sys.stdin.readline().split()))) 

# print(info)

for i in range(N):
    if info[i][0] == "push":
        # print("push")
        q.append(info[i][1])
    elif info[i][0] == "top":
        # print("top")
        if len(q) == 0:
            print(-1)
        else:
            print(q[len(q)-1])
           
    
    elif info[i][0] == "size":
        # print("size")
        print(len(q))
    elif info[i][0] == "empty":
        # print("empty")
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif info[i][0] == "pop":
        # print("pop")
        if len(q) == 0:
            print(-1)
        else:
            print(q[len(q)-1])
            q.pop()
    