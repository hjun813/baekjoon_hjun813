##########################################################################
import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
M = input().strip()
tree = {i: [] for i in range(N + 1)}
place = [0] * (N + 1)
visited = [False] * (N + 1)
answer = 0

for i in range(len(M)):  # 실내&실외 정보 int 저장
    if M[i] == "1":
        place[i + 1] = 1

for _ in range(N - 1):  # 길 정보 저장
    node1, node2 = map(int, input().split())
    tree[node1].append(node2)
    tree[node2].append(node1)

for i in tree:
    tree[i].sort()

print(tree)

def dfs(v):  # v와 연결된 1의 개수 0일때는 거 가서 연결된 1개수 까지
    result = 0
    for i in tree[v]:
        if place[i] == 0:
            if not visited[i]:
                visited[i] = True
                result += dfs(i)
        else:
            result += 1
    return result


for i in range(1, N + 1):
    if place[i] == 0:  # 지금 0이면 dfs써서 찾기
        if not visited[i]:
            visited[i] = True
            a = dfs(i)
            answer += a * (a - 1)
    elif place[i] == 1:  # 지금 1이면 연결된 1 있는지 찿기
        for check in tree[i]:
            if place[check] == 1:
                answer += 1

print(answer)
