# import sys
# N = int(sys.stdin.readline())

# numList = list(map(int, sys.stdin.readline().split()))

# numLenList = []

# def lengthCheck(n, arr):
#     for i in range(n):
#         if arr[i] < arr[n]:

#             numLenList.append(lengthCheck(i, arr) + 1)
#     numLenList.append(1) 
#     return 1


# lengthCheck(N-1, numList)
# # for i in range(N):
# #     numLenList[i] = lengthCheck(i, numList)
# print(numLenList)
# print(max(numLenList))

n = int(input())
arr = list(map(int, input().split()))

dp = [1] * n  

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:  
            dp[i] = max(dp[i], dp[j] + 1) 

print(max(dp))  
