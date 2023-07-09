N, M = map(int, input().split())
card = list(map(int, input().split()))

sum = 0
for i in range (N - 2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            card_sum = card[i] + card[j] + card[k]
            if card_sum <= M and card_sum > sum:
                sum = card_sum
print(sum)