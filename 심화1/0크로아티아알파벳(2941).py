A = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

count = 0
index = 0

while index < len(A):
    if A[index:index+2] in croatia:
        count += 1
        index += 2
    elif A[index:index+3] in croatia:
        count += 1
        index += 3
    else:
        count += 1
        index += 1
print(count)