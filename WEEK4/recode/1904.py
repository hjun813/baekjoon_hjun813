import sys
input = sys.stdin.readline
N = int(input())
dp = [0] * (N + 1)
dp[0] = 1
dp[1] = 1


def tile(n):
    if n == 0:
        return dp[0]
    elif n == 1:
        return dp[1]
    else:
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
            dp[i] = dp[i] % 15746


tile(N)
print(dp[N])
