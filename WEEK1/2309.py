dwarf = []

for i in range(0,9):
    dwarf.append(int(input()))


# print(allHeight)

#============================================================================
# 2명 키 빼주기
for i in range(0,9):
    if len(dwarf) == 9:    
        allHeight = sum(dwarf)
        # s
        allHeight = allHeight - dwarf[i]
        all2Height = allHeight
        for j in range(0,9):
            allHeight = all2Height
            if i != j:
                #똑같은 난쟁이 뺴주지 않기
                
                # print(allHeight,dwarf[j])
                allHeight = allHeight - dwarf[j]
                # print(allHeight)
                if allHeight == 100:

                    fake1=dwarf[i]
                    fake2 = dwarf[j]
                    dwarf.remove(fake1)
                    dwarf.remove(fake2)
                    dwarf.sort()
                    for v in range(7):
                        print(dwarf[v])
                    
                    break
                    # i 번째랑 j 번째 뺴고 나머지
                else :
                    # allHeight = allHeight - dwarf[i]
                    continue

#============================================================================

