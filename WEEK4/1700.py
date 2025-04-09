import sys
input = sys.stdin.readline

N, K = map(int, input().split())
use = list(map(int, input().split()))
useName = set(use)
# print(use)
# print(useName)
count = 0
multi = []

for i in range(len(use)):
    # print(use[i])
    # print('m', multi)
    if len(multi) < N:
        if use[i] not in multi:
            multi.append(use[i])
        else: 
            continue
    else: # 플러그 다찼을때
        # print("뽑기 ")
        if use[i] in multi:
            continue
        else:
            number = []
            for multiN in multi:
                if multiN not in use[i+1:]:
                    # print('!!', multiN)
                    multi.remove(multiN)
                    multi.append(use[i])
                    count += 1
                    break
                else:
                    
                    for k in range(i+1, K):
                        if multiN == use[k]:
                            number.append(k)
                            break
            # print("zzzz")
            # print(number)
            if len(number) == N:
                # print("뽑")
                if len(number) != 1:
                    maxV = max(number)
                    for j in range(len(number)):
                        if number[j] == maxV:
                            # print("뽑아요", multi[j])
                            multi.remove(multi[j])
                            break
                    # print()
                    multi.append(use[i])
                    
                    count += 1
                else:
                    multi.remove(multi[0])
                    multi.append(use[i])
                    
                    count += 1
print(count)