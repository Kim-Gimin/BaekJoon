def MeanofPassion(A, n):
    sum = 0
    for i in range (1, n):
        sum += A[i]
    return sum
    
n = int(input())
A = [i for i in range (n)]
MeanofPassion(A, n)
print(n)
print(1)