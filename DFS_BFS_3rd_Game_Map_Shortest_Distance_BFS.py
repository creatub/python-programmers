from collections import deque

def solution(maps):
    return findShortestDistance(maps)

def findShortestDistance(maps):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque([(0, 0, 1)])  # 시작 위치와 이동 거리를 큐에 추가

    while queue:
        x, y, distance = queue.popleft()

        if x == len(maps) - 1 and y == len(maps[0]) - 1:
            return distance  # 도착 지점에 도달했을 때 거리를 반환

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] == 1:
                maps[nx][ny] = 0  # 방문한 위치 표시
                queue.append((nx, ny, distance + 1))  # 다음 위치와 거리를 큐에 추가

    return -1  # 도착 지점에 도달할 수 없는 경우
