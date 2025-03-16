# Z

   
def number(a, n, j):
    mul, rest = 0 , 0
    if a == 0:
        return 0

    for i in range(0, n+2):
        if 2**(i) <= a and a < 2**(i+1):
            mul = i
            rest = a - 2**i
            if rest == 0 :
                return 2**(mul*2+j)
            
            else : 
                return 2**(mul*2+j) + number(rest, mul,j)






info = list(map(int, input().split()))
N = info[0] 
r = info[1]
c = info[2]



r_num = number(r,N,1)
c_num = number(c,N,0)

# print("=============")
# print(r_num)
# print(c_num)
print(r_num + c_num)




