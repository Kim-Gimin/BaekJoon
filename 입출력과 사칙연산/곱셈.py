# A = int(input())
# B = int(input())

# result_1 = A * (B % 10)
# result_2 = A * ((B // 100) % 10)
# result_3 = A * (B // 100)
# result_4 = A * B

# print(result_1)
# print(result_2)
# print(result_3)
# print(result_4)

num1 = int(input())
num2 = int(input())

result3 = num1 * (num2 % 10)
result4 = num1 * ((num2 // 10) % 10)
result5 = num1 * (num2 // 100)
result6 = num1 * num2

print(result3)
print(result4)
print(result5)
print(result6)