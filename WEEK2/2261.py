import sys

n = int(sys.stdin.readline())
point = []

for i in range(n):
    point.append(list(map(int, sys.stdin.readline().split())))

point.sort()  # 점 x좌표로 정렬


def findMin(arr):  # divide 한 부분에서(2~3 개의 점) 최소길이 구하기

    minLen = float("inf")
    if len(arr) == 2:
        a = (arr[0][0] - arr[1][0]) ** 2 + (arr[0][1] - arr[1][1]) ** 2
        minLen = min(minLen, a)
        return minLen
    
    elif len(arr) == 3:
        return min(
            (arr[0][0] - arr[1][0]) ** 2 + (arr[0][1] - arr[1][1]) ** 2,
            (arr[0][0] - arr[2][0]) ** 2 + (arr[0][1] - arr[2][1]) ** 2,
            (arr[1][0] - arr[2][0]) ** 2 + (arr[1][1] - arr[2][1]) ** 2,
        )
    


def dividePoint(start, end):  # 점들 반으로 나눠서 최소값 비교 후 최소값 리턴

    if end - start == 1 or end - start == 2:
        return findMin(point[start : end + 1])

    else:
        mid = (start + end) // 2

        left, right = dividePoint(start, mid), dividePoint(mid + 1, end)  # 왼쪽 최소, 오른쪽 최소
        need = []
        firstMin = min(left, right)

        for i in range(start, end + 1):
            if (
                point[mid][0] - int((firstMin) ** (1 / 2)) - 1 <= point[i][0]
                and point[i][0] <= point[mid][0] + int((firstMin) ** (1 / 2)) + 1
            ):
                need.append(point[i])  # 비교 필요한 점 배열에 넣어버리기

        need.sort(key=lambda x: x[1])  # y좌표 기준 정렬!!!!!

        for i in range(len(need)):
            for j in range(i + 1, len(need)):
                if (need[j][1] - need[i][1]) ** 2 >= firstMin:
                    break  # y좌표 차이가 최솟값보다 커지면 체크 할 필요가 없음
                
                firstMin = min(
                    firstMin,
                    (need[i][0] - need[j][0]) ** 2 + (need[i][1] - need[j][1]) ** 2,
                )

        return firstMin


print(dividePoint(0, n - 1))
