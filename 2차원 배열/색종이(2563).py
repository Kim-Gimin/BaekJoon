N = int(input())
canvas = [[0] * 100 for _ in range(100)]


for i in range (N):
    x, y = map(int, input().split())
    
    left = x
    right = x + 10
    bottom = y
    top = y + 10
    
    for i in range (left, right):
        for j in range (bottom, top):
            canvas[i][j] = 1
            
area = sum(sum(row) for row in canvas)
print(area)

