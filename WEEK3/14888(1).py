N = int(input())
number = list(map(int, input().split()))
operators = list(map(int, input().split()))

mx = -1e9
mn = 1e9

def dfs(n, temp):
    global mx, mn

    # 종료 조건
    if n == N - 1:
        mx = max(temp, mx)
        mn = min(temp, mn)
        return

    # 하부함수 호출
    if operators[0] != 0:  # 덧셈하는 경우
        operators[0] -= 1
        dfs(n + 1, temp + number[n + 1])
        operators[0] += 1

    if operators[1] != 0:  # 뺄셈하는 경우
        operators[1] -= 1
        dfs(n + 1, temp - number[n + 1])
        operators[1] += 1

    if operators[2] != 0:  # 곱셈하는 경우
        operators[2] -= 1
        dfs(n + 1, temp * number[n + 1])
        operators[2] += 1

    if operators[3] != 0:  # 나눗셈하는 경우
        operators[3] -= 1
        dfs(n + 1, int(temp / number[n + 1]))
        operators[3] += 1

dfs(0, number[0])
print(mx)
print(mn)
