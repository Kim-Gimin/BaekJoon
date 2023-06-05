T = int(input())
for _ in range(T):
    R, S = input().split()
    R = int(R)
    S = list(S)
    SS = [item for item in S for _ in range(R)]
    SSS = ''.join(SS)
    print(SSS)