import sys
from collections import deque

N = int(sys.stdin.readline())
info = []
a = []
q = deque(a)


for i in range(N):
    info.append(list(map(str, sys.stdin.readline().split())))



for i in range(N):
    if info[i][0] == "push":
       
        q.append(info[i][1])
    elif info[i][0] == "front":
    
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif info[i][0] == "back":
        
        if len(q) == 0:
            print(-1)
        else:
            print(q[len(q) - 1])
    elif info[i][0] == "size":
        
        print(len(q))
    elif info[i][0] == "empty":
       
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif info[i][0] == "pop":
     
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
            q.popleft()
