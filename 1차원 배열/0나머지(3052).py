count = set()
for _ in range (10):
    i = int(input())
    num = i % 42
    count.add(num)
counts = len(count)
    
print(counts)