import sys
input = sys.stdin.readline
N = int(input())

dp = {}

for i in range(1, N+1):
    if i == 1:
        dp[i] = 0
    elif i == 2:
        dp[i] = 1
    elif i == 3:
        dp[i] = 1
    else:
        if i % 3 == 2:
            dp[i] = dp[i-2] + 2
        elif i % 3 == 1:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = dp[i/3] + 1

        if i % 2 == 1:
            dp[i] = min(dp[i], dp[i-1] + 1)
        else:
            dp[i] = min(dp[i], dp[i/2] + 1)



print(dp[N])