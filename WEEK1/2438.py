i = int(input())
j = 0

while j < i:
    j = j + 1
    for p in range(0, j):
        print("*", end="")
    print("")