import sys
input = sys.stdin.readline
n = int(input())

dp = [0 for _ in range(n+2)]
dp[1] = 1
dp[2] = 2
if n > 2:
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
        dp[i] = dp[i] % 10007
    print(dp[n])
elif n == 2:
    print(dp[2])
elif n ==1:
    print(dp[1])

##################################
# import sys

# input = sys.stdin.readline
# n = int(input())

# dp = [0 for _ in range(n + 2)]
# dp[1] = 1
# dp[2] = 2


# def tile(n):
#     if n == 1:
#         return dp[1]
#     elif n == 2:
#         return dp[2]
#     else:
#         if dp[n] != 0:
#             return dp[n]
#         else:
#             dp[n] = tile(n - 1) + tile(n - 2)
#             dp[n] = dp[n] % 10007
#             return dp[n]


# print(tile(n))
