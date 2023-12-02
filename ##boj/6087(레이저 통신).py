import sys
from heapq import heappush, heappop

direction = [[-1, 0], [0, -1], [1, 0], [0, 1]]

In = sys.stdin.readline

W, H = map(int, In()[:-1].split(' '))

laser_map = [['.' for _ in range(W)] for _ in range(H)]
laser_mirror_count_map = [
    [sys.maxsize] * W for _ in range(H)
]
laser_map_visited = [[[False, False] for _ in range(W)] for _ in range(H)]

heap_queue = []

for i in range(H - 1, -1, -1):
    for j, char in enumerate(list(In()[:-1])):
        laser_map[i][j] = char

for i in range(H):
    for j in range(W):
        if laser_map[i][j] == 'C':
            heappush(heap_queue, (-1, i, j))
            laser_map[i][j] = '*'

        while heap_queue:
            mirror_count, x, y = heappop(heap_queue)
            mirror_count += 1

            for dir_i, dir_v in enumerate(direction):
                dir_x, dir_y = dir_v
                cur_x, cur_y = x, y
                while True:
                    next_x = cur_x + dir_x
                    next_y = cur_y + dir_y

                    # print(next_x, next_y)
                    if 0 <= next_x < H and 0 <= next_y < W:
                        if laser_map[next_x][next_y] == '.':
                            direction_key = 0 if dir_i % 2 == 1 else 1

                            if laser_mirror_count_map[next_x][next_y] > mirror_count or \
                                    (laser_mirror_count_map[next_x][next_y] == mirror_count and not
                                    laser_map_visited[next_x][next_y][direction_key]):

                                laser_map_visited[next_x][next_y][direction_key] = True

                                if laser_mirror_count_map[next_x][next_y] > mirror_count:
                                    laser_mirror_count_map[next_x][next_y] = mirror_count

                                heappush(heap_queue, (mirror_count, next_x, next_y))

                                cur_x, cur_y = next_x, next_y
                            else:
                                break

                        if laser_map[next_x][next_y] == '*':
                            break

                        if laser_map[next_x][next_y] == 'C':
                            print(mirror_count)
                            exit()
                    else:

                        break
