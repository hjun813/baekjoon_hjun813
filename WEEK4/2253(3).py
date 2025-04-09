import sys

input = sys.stdin.readline

N, M = map(int, input().split())
small = []
for _ in range(M):
    small.append(int(input()))

dp = [[float("inf")] * (int((2 * N) ** (1 / 2)) + 2) for _ in range(N + 1)]

# 점화식 : dp[i][j] : i 는 위치, j는 점프 -> 최소횟수 반환
# dp[i][j] = min(dp[i-j][j-1], dp[i-j][j], dp[i-j][j+1]) + 1

dp[1][0] = 0  # 시작점

for i in range(2, N + 1):
    if i in small:
        continue
    else:
        for j in range(1, int((2 * i) ** (1 / 2)) + 1):
            dp[i][j] = min(dp[i - j][j - 1], dp[i - j][j], dp[i - j][j + 1]) + 1

if min(dp[N]) == float("inf"):
    print(-1)
else:
    print(min(dp[N]))
