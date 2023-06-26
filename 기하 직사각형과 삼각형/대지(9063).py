import sys

# 입력 받기
n = int(sys.stdin.readline())
points = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    points.append((x, y))

# x, y 좌표의 최소/최대값 찾기
min_x = min(points, key=lambda p: p[0])[0]
max_x = max(points, key=lambda p: p[0])[0]
min_y = min(points, key=lambda p: p[1])[1]
max_y = max(points, key=lambda p: p[1])[1]

# 넓이 계산
width = max_x - min_x
height = max_y - min_y
area = width * height

# 결과 출력
print(area)
