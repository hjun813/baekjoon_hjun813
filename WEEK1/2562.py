len = 9
num_list = list()

for i in range(len):
    num_list.append(int(input()))
    
print(max(num_list))


for i in range(len):
    if max(num_list) == num_list[i]:
        print(i + 1)
