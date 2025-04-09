# ============================1991==================================
# N = int(input())
# tree = {}

# class Node:
#     def __init__(self, item, left, right):
#         self.item = item
#         self.left = left
#         self.right= right

# for _ in range(N):
#     node, left, right = map(str, input().split())
#     tree[node] = Node(node, left, right)

# def preorder(node):

#     if node.item != '.':
#         print(node.item)
#     if node.left != '.':
#         preorder(tree[node.left])
#     if node.right != '.':
#         preorder(tree[node.right])

# preorder(tree['A'])
# ===============================================================

# =============================5639==================================

# import sys

# sys.setrecursionlimit(10**5)

# pre = []
# while True:
#     try:
#         pre.append(int(sys.stdin.readline()))
#     except:
#         break


# def prepost(start, end):

#     if start > end:
#         return

#     mid = end + 1

#     for i in range(start + 1, end + 1):
#         if pre[i] > pre[start]:
#             mid = i
#             break

#     prepost(start + 1, mid - 1)
#     prepost(mid, end)
#     print(pre[start])


# prepost(0, len(pre) - 1)
# ======================================================================

# #============================1991========================================
# import sys
# input = sys.stdin.readline

# N = int(input())

# class Node:
#     def __init__(self, item, left, right):
#         self.item = item
#         self.left = left
#         self.right = right

# tree = {}

# for i in range(N):
#     item, left, right = map(str, input().split())
#     tree[item] = Node(item, left, right)

# def preorder(v):
#     if v != '.':
#         print(v.item)
#     if v.left != '.':
#         preorder(tree[v.left])
#     if v.right != '.':
#         preorder(tree[v.right])

# preorder(tree['A'])
# #============================================================================

# ==================================5639=======================================
# import sys
# sys.setrecursionlimit(10**5)
# input = sys.stdin.readline

# pre = []

# while True:
#     try:
#         pre.append(int(input()))
#     except:
#         break

# def prepost(start, end):

#     if start > end:
#         return
#     mid = end + 1
#     for i in range(start + 1, end+1):
#         if pre[i] > pre[start]:
#             mid = i
#             break

#     prepost(start + 1, mid -1)
#     prepost(mid, end)
#     print(pre[start])

# prepost(0, len(pre)-1)
# ===================================================================================

# ====================================1260==========================================
import sys
input = sys.stdin.readline
from collections import deque

N, M, V = map(int, input().split())

tree = {i : [] for i in range(N + 1)}
visitedDfs = [False] * (N+1)
resultDfs = []
visitedBfs = [False] * (N+1)
resultBfs = []

for _ in range(M):
    node1, node2 = map(int, input().split())
    tree[node1].append(node2)
    tree[node2].append(node1)

for i in tree:
    tree[i].sort()

# print(tree)

def dfs(v):
    visitedDfs[v] = True
    resultDfs.append(v)
    for i in tree[v]:
        if not visitedDfs[i]:
            dfs(i)

dfs(V)
print(*resultDfs)


def bfs(v):
    queue = deque([v])
    visitedBfs[v] = True
    while queue:
        k = queue.popleft()
        resultBfs.append(k)
        for i in tree[k]:
            if not visitedBfs[i]:
                queue.append(i)
                visitedBfs[i] = True

bfs(V)
print(*resultBfs)
# ======================================================================

# =============================11724====================================
# import sys

# input = sys.stdin.readline
# N, M = map(int, input().split())
# tree = {i: [] for i in range(N + 1)}
# visited = [False] * (N + 1)
# count = 0

# for _ in range(M):
#     node1, node2 = map(int, input().split())
#     tree[node1].append(node2)
#     tree[node2].append(node1)

# for i in tree:
#     tree[i].sort()

# # print(tree)

# def connected(v):
#     visited[v] = True
#     for i in tree[v]:
#         if not visited[i]:
#             connected(i)
#             visited[i] = True

# for i in range(1, N + 1):
#     if not visited[i]:
#         connected(i)
#         count += 1

# print(count)
# # ======================================================================
#
# # ============================2606======================================
# import sys
# from collections import deque
# input = sys.stdin.readline

# N = int(input())
# M = int(input())

# graph = {i: [] for i in range(N + 1)}
# visited = [False] * (N+1)
# result = []

# for _ in range(M):
#     node1, node2 = map(int, input().split())
#     graph[node1].append(node2)
#     graph[node2].append(node1)

# for i in graph:
#     graph[i].sort()

# # print(graph)

# def dfs(v):
#     visited[v] = True
#     result.append(v)
#     for i in graph[v]:
#         if not visited[i]:
#             dfs(i)

# def bfs(v):
#     queue = deque([v])
#     visited[v] = True
#     while queue:
#         k = queue.popleft()
#         for i in graph[k]:
#             if not visited[i]:
#                 visited[i] = True
#                 queue.append(i)
#                 result.append(i)


# # dfs(1)
# # print(len(result) - 1)
# bfs(1)
# print(len(result))
# # ======================================================================


# # =============================11725====================================
# import sys
# from collections import deque
# input = sys.stdin.readline

# N = int(input())
# tree = {i: [] for i in range(N + 1)}
# parent = [0] * (N + 1)

# for _ in range(N - 1):
#     node1, node2 = map(int, input().split())
#     tree[node1].append(node2)
#     tree[node2].append(node1)

# for i in tree:
#     tree[i].sort()

# # print(tree)

# def bfs(v):
#     queue = deque([v])
#     while queue:
#         k = queue.popleft()
#         for i in tree[k]:
#             if parent[i] == 0:
#                 parent[i] = k
#                 queue.append(i)

# bfs(1)
# for i in range(2, N + 1):
#     print(parent[i])

import sys
from collections import deque

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
tree = {i: [] for i in range(N + 1)}

place = list(input().strip())  # 입력값을 받아서 공백 제거
place.insert(0, "0")  # 인덱스 맞추기 위해 앞에 '0' 추가

for _ in range(N - 1):
    node1, node2 = map(int, input().split())
    tree[node1].append(node2)
    tree[node2].append(node1)

visited = [False] * (N + 1)

def count_edges(v):
    
    stack = [v]
    visited[v] = True
    one_nodes = 1  # '1' 노드 개수
    edges = 0

    while stack:
        cur = stack.pop()
        for nxt in tree[cur]:
            if not visited[nxt] and place[nxt] == "1":
                visited[nxt] = True
                stack.append(nxt)
                one_nodes += 1
                edges += 1  # '1' 노드끼리 연결되는 간선 수 증가
    return one_nodes * (one_nodes - 1) // 2  # 조합 공식 nC2

result = 0
for i in range(1, N + 1):
    if place[i] == "1" and not visited[i]:
        result += count_edges(i)

# '1'과 인접한 '0' 노드 개수 세기
for i in range(1, N + 1):
    if place[i] == "1":
        for nxt in tree[i]:
            if place[nxt] == "0":
                result += 1  # '1'과 '0'을 연결하는 경우는 단순히 개수를 더해줌

print(result*2)

