# while True:
#     A,B = map(int, input().split())
#     print(A + B)
#     break
import sys
for line in sys.stdin:
    A,B = map(int, line.split())
    print(A+B)