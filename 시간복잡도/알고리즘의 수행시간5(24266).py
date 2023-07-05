def MeanOfPassion(A, n):
    sum = 0
    for i in range (1, n):
        for j in range(1, n):
            for k in range(1, n):
                sum += A[i] * A[j] * A[k]
                
    return sum
n = int(input())
A = [i for i in range (n)]
print(n*n*n)
print(3)