import sys
from collections import deque

N = int(sys.stdin.readline())

tower = list(map(int, sys.stdin.readline().split()))
lazer = []
index = []
result = [0] * N
# tower.reverse()
q = deque(tower)

while len(q) > 0:


    # print("q", q)
    # print("lazer", lazer)
    
    # print("index!!", index)
    next = q.pop()
    # print("next", next)
    nextIndex = len(q)
    # print("nextIndex", nextIndex)
    # print()

    if len(lazer) != 0:
        if next < lazer[-1]: 
            lazer.append(next)
            index.append(len(q))
        else:
            while len(lazer) != 0:
                if lazer[-1] < next:
                    # print("hello pop here!!!", lazer[-1])
                    lazer.pop()
                    lazerIndex = index.pop()
                    result[lazerIndex] = nextIndex +1
                else :
                    break
           
            lazer.append(next)
            index.append(len(q))
 
            # print("레이저!!!", lazer[-1])
            
            

    else:
        lazer.append(next)
        index.append(len(q))
       

# print("lazer", lazer)
# print("index!!", index)
# print("result!!", result)
for i in result:
    print(i, end=" ")

# Monotonic Stack - 단조 감소 스택을 하면 배열 순서로 자기보다 큰 값을 얻을 수 있다.