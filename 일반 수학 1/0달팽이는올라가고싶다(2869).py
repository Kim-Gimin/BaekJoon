"""
def climb(A,B,V):
    t = 0
    count = 0
    result = 0
    while True:
        t += A
        count += 1
        if t >= V:
            return count
        else:
            t -= B
            
A, B, V = map(int, input().split())

Day = climb(A,B,V)

print(Day)
"""

A, B, V = map(int, input().split())
k = (V - B)/(A - B)
if k == int(k):
    print(int(k))
else:
    j = int(k) + 1
    print(int(j))