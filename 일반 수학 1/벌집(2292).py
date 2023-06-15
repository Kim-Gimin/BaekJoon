N = int(input())

def find_min_rooms(n):
    if n == 1:
        return 1

    count = 1  # 시작 방(중앙 방)을 포함한 방의 개수
    increment = 6  # 한 바퀴마다 방이 6개씩 증가함
    room = 1  # 현재 방 번호
    while True:
        room += increment
        count += 1
        if n <= room:
            return count
        increment += 6



# 결과 출력
result = find_min_rooms(N)
print(result)
