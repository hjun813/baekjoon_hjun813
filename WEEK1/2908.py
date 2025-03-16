A, B = map(int, input().split(" "))

A_list = list(map(str, str(A)))
A_reversed_list = A_list[::-1]
A_reversed = int("".join(A_reversed_list))

B_list = list(map(str, str(B)))
B_reversed_list = B_list[::-1]
B_reversed = int("".join(B_reversed_list))

print(max(A_reversed, B_reversed))