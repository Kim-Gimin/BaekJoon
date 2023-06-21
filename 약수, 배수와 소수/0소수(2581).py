M = int(input())
N = int(input())

sum = 0
MinPrime = None

def Prime(num):
    if num < 2:
        return False
    for i in range (2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

for num in range(M, N+1):
    if Prime(num):
        sum += num
        if MinPrime is None or num < MinPrime:
            MinPrime = num
if MinPrime is None:
    print(-1)
else:
    print(sum)
    print(MinPrime)