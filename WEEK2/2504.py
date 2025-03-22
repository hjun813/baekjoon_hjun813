import sys
from collections import deque

testcase = list(map(str, sys.stdin.readline()))
result = []
testcase.pop()
q = deque(testcase)
rq = deque(result)
popCheck = 0
rightL, leftL, rightS, leftS = 0, 0, 0, 0
# resultN = 0
resultFinal = []


def check(q, rq):

    resultN = 0
    global rightL, leftL, rightS, leftS
    global popCheck
  

    while len(q) > 0:
        if len(rq) == 0:
            resultFinal.append(resultN)
            resultN = 0
        if rightL <= leftL or rightS <= leftS:

            if q[0] == "(":
                leftS += 1
                rq.append(q[0])
                popCheck = 0
                q.popleft()
                continue

            elif q[0] == ")":
                rightS += 1
                if len(rq)>0:
                    if rq[-1] == "(":
                        rq.pop()
                        if popCheck == 1:
                            resultN = resultN * 2
                            print(resultN)
                        else:
                            resultN = resultN + 2
                            print(resultN)
                        popCheck = 1
                        q.popleft()
                        continue

                        # 계산 맞춰주기
                    else:
                        return print("error!!")
                else:
                    return print("error!!")

            elif q[0] == "[":
                leftL += 1
                rq.append(q[0])
                popCheck = 0
                q.popleft()
                continue

            elif q[0] == "]":
                rightL += 1
                if len(rq)>0:
                    if rq[-1] == "[":
                        rq.pop()
                        if popCheck == 1:
                            resultN = resultN * 3
                            print(resultN)
                        else:
                            resultN = resultN + 3
                            print(resultN)
                        popCheck = 1
                        q.popleft()
                        continue
                        # 계산 맞춰주기
                    else:
                        return print("error")
                else:
                    return print("error")

            # q.popleft()

        else:
            return print(0)

    if rightL != leftL or rightS != leftS:
        return print(0)
    
    print(resultN)

check(q,rq)
# print(rightL, leftL, rightS, leftS)
