import sys
input = sys.stdin.readline
N = int(input())
matrix = []
p = []
for _ in range(N):
    r, c = map(int, input().split())
    matrix.append((r, c))

for i in range(N):
    if i == 0:
        p.append(matrix[i][0])
    p.append(matrix[i][1])

# print(p)
# dp[i][j] : 행렬 i번 부터 j번까지 최소 횟수
# 점화식 dp[i][j] = max(dp[i][j],
#                      dp[i][k] + dp[k+1][j] + 곱한값을 더해야 하는데
#                      이게 곱한 값 맞나? p[i] * p[k+1] * p[j+1]
#                      )
# 풀이에서는 길이가 2인 경우부터 계산해 놓고
# 3인 경우 쭉쭉쭉 계산해서
# 마지막 결과를 얻는 느낌인데

dp = [[0] * N for _ in range(N)]

for length in range(2, N + 1):
    for i in range(N - length + 1):
        j = i + length - 1
        dp[i][j] = float("inf")
        for k in range(i, j):
            dp[i][j] = min(
                dp[i][j], dp[i][k] + dp[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
            )

# print(dp)
print(dp[0][N - 1])
