# import sys
# n = int(input())
# circle_info = []
# stack = []
# count = 1

# for _ in range(n):
#     r, c = list(map(int, sys.stdin.readline().split()))
#     circle_info.append([r - c, '('])
#     circle_info.append([r + c, ')'])
    
# circle_info = sorted(circle_info, key = lambda x : (x[0], -ord(x[1])))

# print(circle_info)

# for i in range(2 * n):

#     print(stack)
#     print('count', count)
#     print()
#     if stack:
#         # 연속으로 open이 들어오고 좌표도 같다면 스택에 있는 open을 내접상태로 바꿔줌
#         if circle_info[i][1] == '(' and circle_info[i][0] == stack[-1]['pos']:
#             stack[-1]['state'] = 2
#         # 시작점 같다면 state 가 2로
#         elif circle_info[i][1] == ')':
#             count += stack.pop()['state'] # 괄호가 닫혀야 카운트로 보냄

#             if not stack:
#                 continue
#             if i + 1 < 2 * n and circle_info[i + 1][0] != circle_info[i][0]: # 다음 원의 시작이 끝나는 곳과 같지 않다면 state 1로 저장
#                 stack[-1]['state'] = 1
#             continue

#     stack.append({'pos': circle_info[i][0], 'shape': circle_info[i][1], 'state': 1})
    
# print(count)

import sys
n = int(input())
circle_info = []
stack = []
count = 1

for _ in range(n):
    r, c = list(map(int, sys.stdin.readline().split()))
    circle_info.append([r - c, '('])
    circle_info.append([r + c, ')'])
    
circle_info = sorted(circle_info, key = lambda x : (x[0], -ord(x[1])))

# 위에는 입력값 받고 받은 입력값은 시작점과 끝점으로 저장함, 이때 시작과 끝을 구분하기 위해 '(' ')' 기호 사용

for i in range(2 * n):

    if stack:
        # 연속으로 open이 들어오고 좌표도 같다면 스택에 있는 open을 내접상태로 바꿔줌
        if circle_info[i][1] == '(' and circle_info[i][0] == stack[-1]['pos']:
            stack[-1]['state'] = 2
        # 시작점 같다면 state 가 2로


        elif circle_info[i][1] == ')':
            count += stack.pop()['state'] # 괄호가 닫혀야 카운트로 보냄

            if not stack:
                continue
            
            if i + 1 < 2 * n and circle_info[i + 1][0] != circle_info[i][0]: # 다음 원의 시작이 끝나는 곳과 같지 않다면 state 1로 저장
                stack[-1]['state'] = 1
            continue

    stack.append({'pos': circle_info[i][0], 'shape': circle_info[i][1], 'state': 1}) #pos: 위치, Shape: 원 시작인지 끝인지, state: 접하는지 아닌지 
    
print(count)