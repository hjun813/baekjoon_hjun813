import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
N, M = map(int, input().split())

ice = []

for i in range(N):
    a = list(map(int, input().split()))
    ice.append(a)

# print(ice)
direction = [(0,-1), (-1, 0), (0,1), (1,0)]

def melting(arr, n):
    newArr = [[[0] for _ in range(M)] for i in range(N)]
    number = icecheck(arr) 

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                newArr[i][j] = 0
            else:
                count = 0
                for x, y in direction:
                    if arr[i+x][j+y] == 0:
                        count += 1
                
                if arr[i][j] - count < 0:
                    newArr[i][j] = 0
                else:
                    newArr[i][j] = arr[i][j] - count

    # 섬 측정했더니 1개면 재귀하고 2개면 몇개인지 리턴
    
    if icecheck(newArr) == 0:
        print(0)
    elif icecheck(newArr) == number:
        melting(newArr,n+1)
    else:
        print(n+1)


def icecheck(arr):
    visited = [[0 for _ in range(M)] for i in range(N)]
    count = 0
    for i in range(N):
        for j in range(M):
            if visited[i][j] == 0:
                if arr[i][j] > 0:
                    dfs(i,j,visited, arr)
                    count += 1
    return count


def dfs(x, y, visited, arr):
    visited[x][y] = 1
    for dx, dy in direction:
        if visited[x+dx][y+dy] == 0:
            if arr[x+dx][y+dy] > 0:
                dfs(x+dx, y+dy, visited, arr)


melting(ice, 0)