a1, a0 = map(int, input().split())
c = int(input())
n = int(input())

fn = lambda n : a1 * n + a0
gn = lambda n : n

result = all(fn(n) <= c * gn(n) for n in range (n, n+100))

print(int(result))