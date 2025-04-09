# import sys

# while True:
#     recInfo = list(map(int, sys.stdin.readline().split()))

#     if len(recInfo) == 1: #0이면 종료
#         break

#     recN = recInfo[0]
#     recHeight = [0] * recN
#     for i in range(recN):
#         recHeight[i] = recInfo[i+1]


# def solution():
#     while True:
#         input_list = map(int, input().replace("\n", '').split())

#         n = next(input_list)
#         if n == 0:
#             break
#         stack = [(-1, -1)]  # (idx, h)
#         max_value = 0

#         for i, h in enumerate(input_list):

#             print("stack", stack)
#             print("check idx", i, "h" , h)
#             if stack[-1][1] < h:
#                 stack.append((i, h))
#                 print("add", (i, h))
#                 print("stack", stack)
#             else:
#                 while stack[-1][1] >= h:
#                     idx, last_h = stack.pop()
#                     print("pop", idx, last_h)
#                     w = i - idx
#                     print('max', max_value, 'new', last_h * w)
#                     max_value = max(max_value, last_h * w)
#                     print('max', max_value)
#                     w_start_i = idx

#                 print("add",(w_start_i, h))
#                 stack.append((w_start_i, h))
#                 print("stack", stack)
#             print()

#         print("remain" , stack)
#         while stack:
#             i, h = stack.pop()
#             w = n - i
#             max_value = max(max_value, h * w)
#             print(max_value)
#         print(max_value)

# solution()


def solution():
    while True:
        input_list = map(int, input().replace("\n", "").split())

        n = next(input_list)
        if n == 0:
            break
        stack = [(-1, -1)]  # (idx, h)
        max_value = 0

        for i, h in enumerate(input_list):

            if stack[-1][1] < h:
                stack.append((i, h))

            else:
                while stack[-1][1] >= h:
                    idx, last_h = stack.pop()
                    w = i - idx
                    max_value = max(max_value, last_h * w)
                    w_start_i = idx

                stack.append((w_start_i, h))

        while stack:
            i, h = stack.pop()
            w = n - i
            max_value = max(max_value, h * w)

        print(max_value)


solution()


# def d_c(histogram, s, e):

#     if s == e:
#         return histogram[e]
#     elif e - s == 1:
#         if histogram[e] < histogram[s]:
#             return max(
#                 2 * histogram[e], histogram[s]
#             )  # s 위치의 높이를 2배하여 넓이 계산
#         else:
#             return max(histogram[e], 2 * histogram[s])
        
#     mid = (s + e) // 2
#     leftarea = d_c(histogram, s, mid)
#     rightarea = d_c(histogram, mid + 1, e)
#     left = mid - 1
#     right = mid + 1
#     midarea = histogram[mid]
#     now_h = histogram[mid]

#     while s <= left and right <= e:
#         if histogram[left] < histogram[right]:
#             if histogram[right] < now_h:
#                 now_h = histogram[right]
#             midarea = max(midarea, now_h * (right - left))
#             right += 1
#         else:
#             if histogram[left] < now_h:
#                 now_h = histogram[left]
#             midarea = max(midarea, now_h * (left - right))
#             left -= 1

#     while s <= left:
#         if histogram[left] < now_h:
#             now_h = histogram[left]
#         midarea = max(midarea, now_h * (right - left))
#         left -= 1

#     while right <= e:
#         if histogram[right] < now_h:
#             now_h = histogram[right]
#         midarea = max(midarea, now_h * (right - left))
#         right += 1
        
#     return max(leftarea, rightarea, midarea)


# result = []
# while True:
#     histogram = list(map(int, input().split()))
#     if histogram[0] == 0:
#         break
#     n = histogram[0]
#     result.append(d_c(histogram, 1, n))
# for i in result:
#     print(i)
