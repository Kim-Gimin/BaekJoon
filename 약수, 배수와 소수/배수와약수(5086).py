while True:
    A, B = map(int, input().split())
    if A == 0:
        break
    elif A > B:
        if A % B == 0:
            print("multiple")
        else:
            print("neither")
    elif A < B:
        if B % A == 0:
            print("factor")
        else:
            print("neither")