N, K = map(int,input().split())
count = []
for i in range (1, N+1):
    if N % i == 0:
        a = [i]
        count.append(a)
    else:
        pass

if len(count) < K :
    print(0)
else:
    print(' '.join(map(str, count[K-1])))
