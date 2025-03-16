snailInfo = list(map(int, input().split(" ")))

A, B, V = (
    snailInfo[0],
    snailInfo[1],
    snailInfo[2],
)

lastHeight = V - A
day = lastHeight / (A - B)
if lastHeight % (A - B) != 0:
   day = day +1
    
print(int(day) + 1)
