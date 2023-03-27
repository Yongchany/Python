import random

# 게임 보드 초기화
board = [[0, 0, 0],
         [0, 0, 0]]

# 캐릭터 위치 초기화
player_row = 0
player_col = 0

# 보물 위치 초기화
treasure_row = 1
treasure_col = 2

# 함정 위치 초기화
trap_row = 1
trap_col = 0

# DFS 함수 정의
def dfs(row, col, visited, count):
    # 현재 위치 방문 처리
    visited[row][col] = True

    # 보물 위치 도달한 경우 반환
    if row == treasure_row and col == treasure_col:
        return True, count

    # 함정 위치 도달한 경우 반환
    if row == trap_row and col == trap_col:
        return False, count

    # 오른쪽으로 이동
    if col < 2 and not visited[row][col+1]:
        count += 1
        found, count = dfs(row, col+1, visited, count)
        if found:
            return True, count

    # 아래로 이동
    if row < 1 and not visited[row+1][col]:
        count += 1
        found, count = dfs(row+1, col, visited, count)
        if found:
            return True, count

    # 위로 이동
    if row > 0 and not visited[row-1][col]:
        count += 1
        found, count = dfs(row-1, col, visited, count)
        if found:
            return True, count

    # 왼쪽으로 이동
    if col > 0 and not visited[row][col-1]:
        count += 1
        found, count = dfs(row, col-1, visited, count)
        if found:
            return True, count

    # 도달할 수 없는 경우 False 반환
    return False, count

# 반복 실행
count = 0
while True:
    # DFS 실행
    visited = [[False, False, False],
               [False, False, False]]
    found, count_per_game = dfs(player_row, player_col, visited, 0)
    count += count_per_game

    # 게임 결과 출력
    if found:
        print("보물을 찾았습니다! (총 %d번 시도)" % count)
        break
    else:
        print("함정에 빠졌습니다. (총 %d번 시도)" % count)
