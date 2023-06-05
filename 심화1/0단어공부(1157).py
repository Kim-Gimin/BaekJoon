A = input().lower()
num = {}
count = 0
max = []

for i in A:
    if i.isalpha():
        num[i] = num.get(i, 0)+1
        if num[i] > count:
            count = num[i]
            max = [i]
        elif num[i] == count:
            max.append(i)
if len(max) > 1:
    print("?")
else:
    print(max[0].upper())