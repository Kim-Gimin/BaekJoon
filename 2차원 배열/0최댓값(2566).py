array1 = [[0 for col in range (9)] for row in range (9)]

for i in range (9):
    num = list(map(int, input().split()))
    for j in range (9):
        array1[i][j] = num[j]
        

max = max(map(max, array1))

for i in range (9):
    for j in range (9):
        if array1[i][j] == max:
            print(max)
            print(i+1, j+1)
            break
        

