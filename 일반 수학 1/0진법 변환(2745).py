N, B = input().split()

B = int(B)
def todemical(N, B):
    digits = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
    d = 0
    p = 0
    
    for digit in N[::-1]:
        if digit.isdigit():
            digit_value = int(digit)
        else:
            digit_value = ord(digit) - ord('A') + 10

        d += digit_value * (B ** p)
        p += 1
    return d
d = todemical(N, B)
print(d)