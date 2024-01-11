from collections import deque
class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def isExit(target: tuple[int]):
            return maze[target[0]][target[1]] == '.' and (
                    (target[0] == 0 or target[0] == len(maze) - 1) or 
                    (target[1] == 0 or target[1] == len(maze[0]) - 1)
                ) and not (
                target[0] == entrance[0] and target[1] == entrance[1])

        def getAdjecent(target: tuple[int]):
            adj = [
                (target[0] + 1, target[1]),
                (target[0] - 1, target[1]),
                (target[0], target[1] + 1),
                (target[0], target[1] - 1)
            ]

            return list(
                filter(
                    lambda x:
                        x[0] >= 0 and
                        x[1] >= 0 and
                        x[0] < len(maze) and
                        x[1] < len(maze[0]) and
                        maze[x[0]][x[1]] == '.',
                    adj 
                )
            )

        distance_map = [[inf for _ in range(len(maze[0]))] for _ in range(len(maze))]

        distance_map[entrance[0]][entrance[1]] = 0

        will_visit = deque([(entrance[0], entrance[1])])
        visited = set()

        while will_visit:

            current_space = will_visit.popleft()

            # if current_space in visited:
            #     continue

            distance = distance_map[current_space[0]][current_space[1]]

            for next in getAdjecent(current_space):
                if isExit(next):
                    return distance + 1
                if next not in visited:
                    if distance_map[next[0]][next[1]]> distance + 1:
                        distance_map[next[0]][next[1]] = distance + 1
                        will_visit.append(next)
                        

            visited.add(current_space)


        return -1
   
        

        
