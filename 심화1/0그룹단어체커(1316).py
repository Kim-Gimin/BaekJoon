A = int(input())
count = 0

for _ in range (A):
    a = input()
    isgroup = True
    used = set()
    prev = None
    for char in a:
        if prev is None or char == prev:
            used.add(char)
            prev = char
        else:
            if char in used:
                isgroup = False
                break
            else:
                used.add(char)
                prev = char
    if isgroup:
        count += 1
print(count)