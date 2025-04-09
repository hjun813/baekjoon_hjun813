import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * (N+2)
dp[1] = 1
dp[2] = 2


def tile():
    if N ==1:
        return dp[1]
    if N == 2:
        return dp[2]
    else:
        for i in range(3,N+1):
            dp[i] = dp[i-1] + dp[i-2]
            dp[i] = dp[i] % 15746

tile()
print(dp[-2])
## 
