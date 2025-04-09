import sys

input = sys.stdin.readline
thing = [(0,0)]
N, K = map(int, input().split())
for _ in range(N):
    weight, value = map(int, input().split())
    thing.append((weight, value))

dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

# print(thing)
for i in range(1,N+1):
    for j in range(1, K+1):
        if thing[i][0] > j:
            dp[i][j] = dp[i-1][j]
        elif thing[i][0] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-thing[i][0]]+thing[i][1])

print(dp[-1][-1])
# for i in range(N+1):
#     print(dp[i])