import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

A = input().rstrip()
tree = {i: [] for i in range(N + 1)}
place = [0] * (N+1)
visited = [0] * (N+1)

for i in range(len(A)):
    if A[i] == '1':
        place[i+1] = 1

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
    
def dfs(node): 
    res = 0 
    for next_node in tree[node]:
        if place[next_node] == 0:
            if not visited[next_node]:
                visited[next_node] = 1
                res += dfs(next_node)
        else:
            res += 1
    return res

ans = 0

for i in range(1, N+1):
    if place[i] == 0:
        if not visited[i]:
            visited[i] = 1
            res = dfs(i)
            ans += res * (res - 1)
    else:
        for next_node in tree[i]:
            if place[next_node] == 1:
                ans += 1
print(ans)