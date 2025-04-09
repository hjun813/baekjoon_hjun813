import sys
input = sys.stdin.readline
T = int(input())

def wave(N):
    if N <= 5:
        return dp[N]
    else:
        if dp[N] != 0:
            return dp[N]
        else :
            dp[N] = wave(N-1) + wave(N-5)
            return dp[N]

for _ in range(T):
    N = int(input())
    dp = [0] * (N+5)
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 2
    print(wave(N))
    
