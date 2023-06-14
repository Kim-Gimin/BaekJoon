n = int(input())  # N 입력 받기

ans = 2

for i in range(1, n + 1):
    ans += (ans - 1)

ans = ans ** 2

print(ans)
