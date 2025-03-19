num = int(input())
nQueenPos = [0] * num
nQueenPosHor = [False] * num
nQueenPostive = [False] * (num * 2 - 1)
nQueenNegative = [False] * (num * 2 - 1)
count = 0


def nQueen(num, n):
    global count
    if n < num:

        for i in range(num):

            if not nQueenPosHor[i] and not nQueenPostive[n + i] and not nQueenNegative[n - i + num - 1]:
                nQueenPos[n] = i
                
                nQueenPosHor[i] = True
                nQueenPostive[n + i] = True
                nQueenNegative[n - i + num - 1] = True
                nQueen(num, n + 1)
                nQueenPosHor[i] = False
                nQueenPostive[n + i] = False
                nQueenNegative[n - i + num - 1] = False

    elif n == num:
        # print(nQueenPos)
        count = count+1


nQueen(num, 0)
print(count)

# # #nQueen

# # 1. 한 열당 1개의 퀸 배치 N^N
# # 2. 한 행에 1개의 퀸 배치 N!
# #       바꾼 행에는 True 지정
# # 3. 대각선 배치
# numQ = int(input())


# Queen = [0] * numQ
# verQueenSet = [False] * numQ
# plusDiaQueenSet = [False] * (
#     numQ * 2 - 1
# )  # 2배하는 이유? :느낌상 2개의 대각선 방향을 검사만 하면 되기 때문에 그런가
# minusDiaQueenSet = [False] * (numQ * 2 - 1)
# count = 0


# def printQueen(N):
#     global count
#     for i in range(N):
#         print(Queen[i], "", end="")
#     print()

#     count = count + 1


# def setQ(n, N):
#     for i in range(N):
#         if (
#             not verQueenSet[i]
#             and not plusDiaQueenSet[n + i]
#             and not minusDiaQueenSet[n - i + N - 1]  # 행 체크, 두개의 대각선 체크
#         ):
#             Queen[n] = i

#             if n == N - 1:
#                 printQueen(N)

#             else:
#                 verQueenSet[i] = plusDiaQueenSet[n + i] = minusDiaQueenSet[
#                     n - i + N - 1
#                 ] = True
#                 setQ(n + 1, N)
#                 verQueenSet[i] = plusDiaQueenSet[n + i] = minusDiaQueenSet[
#                     n - i + N - 1
#                 ] = False


# setQ(0, numQ)
# print(count)


