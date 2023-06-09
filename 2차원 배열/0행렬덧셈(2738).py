N, M = list(map(int, input().split()))

array1 = [[0 for col in range(M)] for row in range(N)]
array2 = [[0 for col in range(M)] for row in range(N)]

result = [array1, array2]

for i in range (2):
    arr = result[i]
    for j in range(N):
        number = list(map(int, input().split()))
        for k in range(M):
            arr[j][k] = number[k]
for i in range(N):
    for j in range(M):
        array1[i][j] += array2[i][j]
for i in range(N):
    for j in range(M):
        print(array1[i][j], end=" ")
    print()
    
    