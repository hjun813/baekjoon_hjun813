# import sys

# N, B = map(int, sys.stdin.readline().split())

# arrN = [0] * N
# for i in range(N):
#     arrN[i] = list(map(int, sys.stdin.readline().split()))

# # print(arrN)

# arrM = [[0 for i in range(N)] for j in range(N)]

# # def multMatrix(arr, B):
# # 행렬의 곱

# # for i in range(N):
# #     for j in range(N):
# #         for k in range(N):
# #             arrM[i][j] = arrM[i][j] + (arrN[i][k] * arrN[k][j])

# # print(arrM)


# def multMatrix(arr, B):

#     temp = [[0 for i in range(N)] for j in range(N)]

#     if B == 1:
#         return arr
#     else:
#         for i in range(N):
#             for j in range(N):
#                 for k in range(N):
#                     temp[i][j] += (arr[i][k] * arr[k][j])

#         for i in range(N):
#             for j in range(N):
#                 temp[i][j] = temp[i][j] % 1000

#         if B % 2 == 1:
#             tempArr = multMatrix(temp, (B - 1) // 2) 
            
#             tempN = [[0 for i in range(N)] for j in range(N)]
#             for i in range(N):
#                 for j in range(N):
#                     for k in range(N):
#                         tempN[i][j] += (tempArr[i][k] * arr[k][j])

#             for i in range(N):
#                     for j in range(N):
#                         tempN[i][j] = tempN[i][j] % 1000
#             return tempN
        
#         else:
#             return multMatrix(temp, B // 2)

# result = multMatrix(arrN, B)

# for i in range(N):
#     for j in range(N):
#         print(result[i][j] % 1000, end=" ")
#     print()


import sys

N, B = map(int, sys.stdin.readline().split())

arrN = [0] * N

for i in range(N):
    arrN[i] = list(map(int, sys.stdin.readline().split()))


def multMatrix(arr1, arr2):  # arr1 과 arr2 행렬 곱하기 -> 행렬 반환

    temp = [[0 for i in range(N)] for j in range(N)]

    for i in range(N):
        for j in range(N):
            for k in range(N):
                temp[i][j] += arr1[i][k] * arr2[k][j]

    for i in range(N):
        for j in range(N):
            temp[i][j] = temp[i][j] % 1000

    return temp


def solve(arr, B): # arr 행렬 B제곱 결과 반환

    if B == 1:
        return arr
    else:
        if B % 2 == 0:  # arr^B -> (arr^2)^(B//2) B가 짝수
            squareArr = multMatrix(arr, arr)
            return solve(squareArr, B // 2)

        elif B % 2 == 1: # arr^B -> (arr^2)^((B-1)//2) B가 홀수
            squareArr = multMatrix(arr, arr)
            tmp = solve(squareArr, (B - 1) // 2)
            return multMatrix(tmp, arr)
        

result = solve(arrN, B)

for i in range(N):
    for j in range(N):
        print(result[i][j] % 1000, end=" ")
    print()