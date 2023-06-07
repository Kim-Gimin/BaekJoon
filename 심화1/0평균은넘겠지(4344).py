C = int(input())

for _ in range (C):
    data  = list(map(int, input().split()))
    N = data[0]
    score = data[1:]
    
    average = sum(score) / N
    
    up = len([A for A in score if A > average ])
    
    ratio = up / N * 100
    print(f"{ratio:.3f}%")