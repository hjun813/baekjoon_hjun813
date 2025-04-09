import sys
input = sys.stdin.readline

N, K = map(int, input().split())
thing = []

for _ in range(N):
    W, V = map(int, input().split())
    thing.append((W,V))

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1,K+1):
        if j < thing[i-1][0]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j- thing[i-1][0]] + thing[i-1][1])

print(dp[-1][-1])