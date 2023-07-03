def MeanOpPassion(A, n):
    sum = 0
    for i in range (1, n):
        sum += A[i] * A[i]
    return sum
n = int(input())
A = [i for i in range(n)]
result = MeanOpPassion(A, n)
d = n*n
print(d)
print(2)