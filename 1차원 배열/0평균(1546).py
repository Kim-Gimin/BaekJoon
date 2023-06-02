import sys
input = sys.stdin.readline

N = int(input())
scores = list(map(int, input().split()))
M = max(scores)

new_s = []
for i in scores:
    new_s.append((i / M) * 100)
    
print(sum(new_s)/N)