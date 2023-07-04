def MeanOfPassion(A, n):
    sum = 0
    for i in range(1, n-1):
        for j in range(i+1, n):
            sum += A[i] * A[i]
    return sum
n = int(input())
A = [i for i in range(n)]



print(n*(n-1)//2)
print(2)