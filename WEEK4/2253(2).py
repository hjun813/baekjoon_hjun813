# BFS 풀이
import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
check = [[] for _ in range(N + 1)] # 방문 체크
small_rock = set()
for _ in range(M):
    small = int(sys.stdin.readline())
    small_rock.add(small)

def solution(N, check, small_rock):
    queue = deque([(1, 0, 0)]) # 위치, 점프, 횟수
    while queue:
        location, jump, n = queue.popleft()
        for x in [jump + 1, jump, jump - 1]:
            if x > 0:
                next_location = location + x # 다음 위치로 점프
                if next_location == N:
                    return n + 1
                if next_location < N and next_location not in small_rock and x not in check[next_location]: #방문체크[다음위치] 에 점프 가 없어야함
                    check[next_location].append(x)
                    queue.append((next_location, x, n + 1))
    return -1 

print(solution(N, check, small_rock))

#######################################################################

# dp 풀이
import sys
N, M = map(int, sys.stdin.readline().split())
dp = [[float('inf')] * (int((2 * N)** 0.5) + 2) for _ in range(N + 1)] # int((2 * N)** 0.5) + 1 이 최대로 점프가능한 길이
dp[1][0] = 0 # dp[위치][점프] => 최소 횟수 반환

stone_set = set()
for _ in range(M):
    stone_set.add(int(sys.stdin.readline()))
    
for i in range(2, N + 1): # i 가 위치
    if i in stone_set:
        continue
    for j in range(1, int((2 * i) ** 0.5) + 1):
        dp[i][j] = min(dp[i - j][j - 1], dp[i - j][j], dp[i - j][j + 1]) + 1 # 점화식 : dp[i][j] = min(dp[i - j][j - 1], dp[i - j][j], dp[i - j][j + 1]) + 1

if min(dp[N]) == float('inf'):
    print(-1)
else:
    print(min(dp[N]))