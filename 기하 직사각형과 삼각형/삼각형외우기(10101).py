a = int(input())
b = int(input())
c = int(input())

if a + b + c == 180:
    if a == b and b == c : 
        print("Equilateral")
    elif (a == b and b != c) or (a == c and b != c) or (b == c and a != b):
        print("Isosceles")
    elif a != b and a != c and b != c:
        print("Scalene")
else:
    print("Error")