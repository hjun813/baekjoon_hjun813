import sys

testcase = sys.stdin.readline()
tmp = 1
answer = 0
stack = []

for i in range(len(testcase)):

    if testcase[i] == "(":
        stack.append(testcase[i])
        tmp = tmp * 2

    elif testcase[i] == "[":
        stack.append(testcase[i])
        tmp = tmp * 3

    elif testcase[i] == ")":
        if not stack or stack[-1] == "[":
            answer = 0
            break
        if testcase[i-1] == "(":
            answer = answer + tmp
        stack.pop()
        tmp = tmp // 2

    elif testcase[i] == "]":
        if not stack or stack[-1] == "(":
            answer = 0
            break
        if testcase[i-1] == "[":
            answer = answer + tmp
        stack.pop()
        tmp = tmp // 3

if stack:
    print(0)
else:
    print(answer)

# array = input()
# tmp = 1
# answer = 0
# stack = []

# for i in range(len(array)):

#     # print("!!", array[i])

#     if array[i] == "(":
#         stack.append(array[i])
#         tmp = tmp * 2
#         # print("tmp",tmp)

#     elif array[i] == "[":
#         stack.append(array[i])
#         tmp = tmp * 3
#         # print("tmp",tmp)

#     elif array[i] == ")":
#         if not stack or stack[-1] == "[":
#             answer = 0
#             break
#         if array[i-1] == "(": # 제일 안쪽 괄호인 경우 더해주기
#             answer = answer + tmp
#         stack.pop()
#         tmp = tmp // 2
#         # print("tmp",tmp)

#     else:
#         if not stack or stack[-1] == "(":
#             answer = 0
#             break
#         if array[i-1] == "[": # 제일 안쪽 괄호인 경우 더해주기
#             answer = answer + tmp
#         stack.pop()
#         tmp = tmp // 3
#     #     print("tmp",tmp)
#     # print("answer", answer)
#     # print()
# if stack:
#     print(0)
# else:
#     print(answer)