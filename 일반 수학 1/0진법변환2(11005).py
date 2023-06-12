N, B = map(int, input().split())


def toN(N, B):
    digits = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z")
    N = int(N)
    if N == 0:
        return "0"
    
    result =""
    while N > 0:
        digit = N % B
        result = digits[digit] + result
        N //= B
    return result
result = toN(N, B)
print(result)