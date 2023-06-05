A, B, C, D, E, F = map(int, input().split())

a = [A, B, C, D, E, F]
b = [1, 1, 2, 2, 2, 8]

c = [bi - ai for ai, bi in zip(a,b)]
print(*c)