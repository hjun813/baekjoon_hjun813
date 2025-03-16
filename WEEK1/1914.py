# 하노이 탑


# n = 원판, a=시작, b=도착, c=보조
def hanoi(n, a, b, c):
    if n == 1:
        print(a, b)
    else:
        hanoi(n - 1, a, c, b)
        print(a, b)
        hanoi(n - 1, c, b, a)


num = int(input())
moving = 2**num - 1
print(moving)

if num <= 20:

    hanoi(num, 1, 3, 2)
