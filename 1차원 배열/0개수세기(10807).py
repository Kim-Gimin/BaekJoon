N = int(input())
numbers = list(map(int, input().split()))
v = int(input())
count = 0
for i in numbers :
    if i == v:
        count += 1

print(count)