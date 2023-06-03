import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    i = input().rstrip()
    print(i[0]+i.strip()[-1])
