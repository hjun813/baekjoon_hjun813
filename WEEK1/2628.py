recInfo = list(map(int,input().split()))
lineNum = int(input())

xInfo = [0]
yInfo = [0]
xLenInfo = []
yLenInfo = []

for i in range(lineNum):
    lineInfo = (input().split(" "))
    if lineInfo[0] == '0' :
        yInfo.append(int(lineInfo[1]))
        #가로선
    else:
        xInfo.append(int(lineInfo[1]))
        #세로선
xInfo.sort()
yInfo.sort()
xInfo.append(recInfo[0])
yInfo.append(recInfo[1])

for i in range(len(xInfo)-1):
    xLenInfo.append(xInfo[i+1] - xInfo[i]) 

for i in range(len(yInfo)-1):
    yLenInfo.append(yInfo[i+1] - yInfo[i]) 

maxSquare = max(xLenInfo) * max(yLenInfo)

print(maxSquare)


