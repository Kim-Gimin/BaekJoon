# A, B, C = map(int, input().split())
# print((A+B)%C)
# print(((A%C)+(B%C))%C)
# print((A*B)%C)
# print(((A%C)*(B%C))&C)

A, B, C = map(int, input().split())

result1 = (A + B) % C
result2 = ((A % C) + (B % C)) % C
result3 = (A * B) % C
result4 = ((A % C) * (B % C)) % C

print(result1)
print(result2)
print(result3)
print(result4)