a = int(input())
b = int(input())

b_1 = b%10
b_2 = (b%100 - b%10)//10
b_3 = (b%1000 - b%100)//100

print(a*b_1)
print(a*b_2)
print(a*b_3)
print(a*b)
