'''
array1 = [[0 for col in range (5)] for row in range (5)]

for i in range (5):
    alpa = list(map(input().split()))
    for j in range (5):
        array1[i][j] = alpa[j]

list(zip(array1))
'''

words = []

for _ in range(5):
    word = input().rstrip()
    words.append(word)
    
result = ""

for j in range (15):
    for i in range(5):
        if j < len(words[i]):
            result += words[i][j]
            
print(result)