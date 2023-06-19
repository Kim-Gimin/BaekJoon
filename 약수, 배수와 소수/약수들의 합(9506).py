while True:
    A = int(input())
    if A != -1:
        list = []
        total = 0
        for i in range(1, A):
            if A % i == 0:
                list.append(i)
                total += i
            else:
                pass
        if A == total:
            equation = f"{A} = " + " + ".join(str(x) for x in list)
            print(equation)
        elif A != total:
            print(A,"is NOT perfect.")
    else:
        break