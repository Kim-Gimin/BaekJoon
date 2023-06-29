while True:
    a, b, c = map(int, input().split())
    list = [a, b, c]
    if a == b == c == 0:
        break
    elif max(list) >= (sum(list) - max(list)):
        print("Invalid")
    else:
        if a == b == c:
            print("Equilateral")
        elif (a == b and a != c) or (a == c and a != b) or (b == c and a != b):
            print("Isosceles")
        elif a != b and a != c and b != c:
            print("Scalene")
    