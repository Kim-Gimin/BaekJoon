def MenOfPassionCount(n):
    count = 0

    for i in range(1, n - 1):
        for j in range(i + 1, n):
            for k in range(j + 1, n + 1):
                count += 1

    return count

def MenOfPassionDegree(n):
    if n <= 2:
        return 0
    elif n <= 3:
        return 1
    elif n <= 4:
        return 2
    else:
        return 3

n = int(input())

count = MenOfPassionCount(n)
degree = MenOfPassionDegree(n)

print(count)
print(degree if degree <= 3 else 4)
