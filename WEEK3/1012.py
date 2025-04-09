import sys
input = sys.stdin.readline

direction = [(1,0),(-1,0),(0,1),(0,-1)]

def dfs(arr, n, visited, M, N, K): # n 배열에서 몇번째, arr 배열
    global total
    visited[n] = True
    x, y = arr[n]
    # dirarr = []
    for a, b in direction:
        if 0<=x+a<M and 0<=y+b<N:
            # dirarr.append((x+a,y+b))
            for i in range(len(arr)):
                if not visited[i]:    
                    if (x+a, y+b) == arr[i]:
                        visited[i] = True
                        dfs(arr, i, visited, M,N,K)


T = int(input())
for _ in range(T):
    total = 0
    M, N, K = map(int, input().split())

    kimchi = []
    for i in range(K):
        x, y = map(int, input().split())
        kimchi.append((x, y))

    # print(kimchi)

    visited = [False] * K

    for i in range(K):
        # print(visited)
        if not visited[i]:
            # print("!!!!!!", i)
            total += 1
            dfs(kimchi, i, visited, M,N,K) 


    print(total)



    
