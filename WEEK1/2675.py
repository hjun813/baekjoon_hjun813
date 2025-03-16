testcase_num = int(input())

for i in range(testcase_num):
    testcase = list(input().split(" "))
    reapeatNum = int(testcase[0])
    text = testcase[1]

    textlist = list(map(str, text))

    for k in range(len(textlist)):
        for j in range(reapeatNum):
            print(textlist[k], end='')
    print('')