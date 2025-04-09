# import sys

# input = sys.stdin.readline

# N = int(input())
# tree = {}

# for i in range(N):
#     node, left, right = input().split()
#     tree[node] = (left, right)

# print(tree)

# def preorder(node, a):
#     left, right = a
#     if node != '.':
#         print(node)
#     if left != '.':
#         preorder(left, tree[left])
#     if right != '.':
#         preorder(right, tree[right])

# preorder('A', tree['A'])
# ============================================================
# import sys
# input = sys.stdin.readline

# V, E = map(int, input().split())

# edge = []
# total = 0
# for _ in range(E):
#     node1, node2, weight = map(int, input().split())
#     edge.append((weight, node1, node2))

# edge.sort()
# parent = [0] * (V+1)
# for i in range(V+1):
#     parent[i] = i

# def find(parent, v):
#     if parent[v] != v:
#         parent[v] = find(parent, parent[v])
#     return parent[v]

# def union(parent, a, b):
#     parent_a = find(parent, a)
#     parent_b = find(parent, b)
#     if parent_a < parent_b:
#         parent[b] = parent[a]
#     else:
#         parent[a] = parent[b]

# for i in edge:
#     cost, a, b = i
#     if find(parent, a) != find(parent, b):
#         union(parent, a, b)
#         total += cost

# print(total)
# ====================================================================
# 1197
# import sys
# sys.setrecursionlimit(10**4)
# input = sys.stdin.readline

# V, E = map(int, input().split())
# edge = []
# total = 0

# for _ in range(E):
#     a, b, weight = map(int, input().split())
#     edge.append((weight, a, b))

# edge.sort()
# parent = [0] * (V + 1)

# for i in range(V + 1):
#     parent[i] = i


# def find(parent, a):
#     if parent[a] != a:
#         parent[a] = find(parent, parent[a])
#     return parent[a]


# def union(parent, a, b):
#     parent_a = find(parent, a)
#     parent_b = find(parent, b)

#     if parent_a < parent_b:
#         parent[parent_b] = parent_a
#     else:
#         parent[parent_a] = parent_b


# for i in range(E):
#     cost, a, b = edge[i]

#     if find(parent, a) != find(parent, b):
#         union(parent, a, b)
#         total += cost

# print(total)
#==============================================================
# import sys
# from collections import deque
# input = sys.stdin.readline

# N = int(input())
# parent = [0] * (N + 1)

# tree = {i: [] for i in range(1, N + 1)}

# for _ in range(N - 1):
#     node1, node2 = map(int, input().split())
#     tree[node1].append(node2)
#     tree[node2].append(node1)

# for node in tree:
#     tree[node].sort()

# print(tree)

# def bfs(v):
#     queue = deque([v])
#     while queue:
#         node = queue.popleft()
#         for child in tree[node]:
#             if parent[child] == 0:
#                 parent[child] = node
#                 queue.append(child)

# bfs(1)


# for i in range(2, N + 1):
#     print(parent[i])
#==============================================================
# import sys
# from collections import deque
# input = sys.stdin.readline
# N, M = map(int, input().split())
# maze = []
# for _ in range(N):
#     mazeLine = list(map(int, input().strip()))
#     maze.append(mazeLine)
# print(maze)
# direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# def bfs():
#     queue = deque([(0,0)])
#     while queue:
#         a, b = queue.popleft()
#         for i in range(4):
#             na, nb = a + direction[i][0], b + direction[i][1]
#             if 0 <= na < N and 0 <= nb < M:
#                 if maze[na][nb] == 1:
#                     queue.append((na, nb))
#                     maze[na][nb] = maze[a][b] + 1

# bfs()
# print(maze[-1][-1])
#======================================================================


