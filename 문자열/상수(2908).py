A, B = input().split()


A1 = A[::-1]
B1 = B[::-1]

A1 = int(A1)
B1 = int(B1)

if A1 > B1:
    print(A1)
else:
    print(B1)
