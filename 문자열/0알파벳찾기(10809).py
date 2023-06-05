S = input()

alphabet = [-1] * 26

for i in range(len(S)):
    index = ord(S[i]) - ord('a')
    if alphabet[index] == -1:
        alphabet[index] = i

for i in range(26):
    print(alphabet[i], end = " ")

    