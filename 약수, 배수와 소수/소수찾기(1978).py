N = int(input())
num = list(map(int, input().split()))
count = 0

for i in range(N):
    if num[i] > 1:
        a = num[i]
        Prime = True
        for j in range(2, a//2 +1):
            if a % j == 0:
                Prime = False
                break
        if Prime:
            count += 1

print(count)
    
