################################다시 풀어보기#################################
import sys

n, c = map(int, sys.stdin.readline().split())
home = []
result = 0

for i in range(n):
    home.append(int(input()))

home.sort()
#########################################################################

low = 1 #최소 거리
high = home[-1] - home[0] #최대 거리

while low <= high:

    mid = (low + high) // 2
    installed = 1
    last_installed = home[0]

    for i in range(1,n):
        if home[i] - last_installed >= mid:
            installed += 1
            last_installed = home[i]

    if installed >= c:
        result = mid
        low = mid +1
    else :
        high = mid -1

print(result)

#==========================================
# 이중탐색을 하는데 간격을 두고
# 정렬된 리스트에서 찾는게 아니라
# 최적의 간격을 찾는 느낌인듯?
# 그 간격이 최소간격일때 배치한 공유기가 많은건 상관 없고 (안 두면 되니까)
# 부족한 경우는 더 둬야할 공간이 없는 거니 다시 찾기
# 
    
