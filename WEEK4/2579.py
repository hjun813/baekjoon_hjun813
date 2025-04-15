import sys

input = sys.stdin.readline

n = int(input())
stairs = []
dp = [[0 for _ in range(3)] for _ in range(n)]

for _ in range(n):
    stair = int(input())
    stairs.append(stair)


dp[-1][1] = stairs[-1]


for i in range(n-2, -1, -1):
    dp[i][0] = max(dp[i+1][2], dp[i+1][1])
    if dp[i+1][0] != 0:
        dp[i][1] = dp[i+1][0] + stairs[i]
    if dp[i+1][1] != 0:
        dp[i][2] = dp[i+1][1] + stairs[i]

print(max(dp[0]))