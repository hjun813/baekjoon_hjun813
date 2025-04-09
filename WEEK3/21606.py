import sys
from collections import deque

sys.setrecursionlimit(10**8)
input = sys.stdin.readline

N = int(input())
tree = {i: [] for i in range(N + 1)}
count = 0
place = list(map(str, input()))
place.pop()
placeQueue = deque(place)
placeQueue.appendleft(0)

for _ in range(N - 1):
    node1, node2 = map(int, input().split())
    tree[node1].append(node2)
    tree[node2].append(node1)

for i in tree:
    tree[i].sort()

# print(placeQueue)
# print(tree)


def walk(v, visited):
    global count
    visited[v] = True
    for i in tree[v]:
        if not visited[i]:
            if placeQueue[i] == "0":
                walk(i, visited)
            elif placeQueue[i] == "1":
                count += 1


for i in range(1, N + 1):
    if placeQueue[i] == "1":
        visited = [False] * (N + 1)
        walk(i, visited)

    # print(count)
    # print()


print(count)
