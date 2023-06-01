X = int(input())
N = int(input())
C = 0
for i in range(N) :
    a, b = map(int, input().split())
    C = C + a * b
    
if C == X:
    print("Yes")
else:
    print("No")
    