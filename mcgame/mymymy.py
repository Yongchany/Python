from collections import deque

# 시작 상태
start_state = {'M': 3, 'C': 3, 'B': 1, 'S': 0}

# 최종 목적
goal_state = {'M': 0, 'C': 0, 'B': 0, 'S': 1}

# 가능한 경우의 수
actions = [('M', -1, 0), ('M', -2, 0), ('M', 1, 0), ('M', 2, 0), ('C', 0, -1), ('C', 0, -2), ('C', 0, 1), ('C', 0, 2), ('MC', -1, -1), ('MC', -2, -2), ('MC', 1, 1), ('MC', 2, 2), ('S', -1, 0), ('S', 1, 0), ('SC', -1, -1), ('SC', 1, 1)]

# 가능한 상태인지 확인하기
def is_valid_state(state):
    # 식인종이 선교사보다 많은지 확인
    if state['M'] < state['C'] and state['M'] > 0:
        return False
    if state['M'] > state['C'] and state['M'] < 3:
        return False
    # 목표 상태보다 작으면 False 반환
    if state['M'] < goal_state['M'] or state['C'] < goal_state['C'] or state['B'] < goal_state['B'] or state['S'] < goal_state['S']:
        return False
    return True

# 상태 변경하기
def change_state(state, action):
    new_state = state.copy()
    # 상태 변경하기
    new_state['M'] += action[1]
    new_state['C'] += action[2]
    new_state['B'] -= action[1] * new_state['B']
    new_state['S'] -= action[2] * new_state['S']
    # 새로운 상태가 유효한지 확인하기
    if is_valid_state(new_state):
        return new_state
    else:
        return None

# 게임 실행하기
def play_game(start_state, goal_state, actions):
    queue = deque()
    queue.append((start_state, []))  # 상태와 경로
    visited = set()
    while queue:
        state, path = queue.popleft()
        if state == goal_state:
            return path
        for action in actions:
            new_state = change_state(state, action)
            if new_state and tuple(new_state.items()) not in visited:
                visited.add(tuple(new_state.items()))
                new_path = path + [action]
                queue.append((new_state, new_path))
    return None

# 게임 시작
print('''
선교사와 식인종이 강을 건너려고 합니다.
보트에는 선교사 또는 식인종 1~2명이 탈 수 있습니다.
하지만 식인종이 선교사보다 많으면 안 됩니다.
모두 반대편으로 옮기는 것이 목표입니다.
''')

#시작 상태 출력
print('시작 상태:')
print(start_state)

#게임 실행
path = play_game(start_state, goal_state, actions)

#결과 출력
if path:
    print('선교사와 식인종을 모두 반대편으로 옮기는 최단 경로:')
    for action in path:
        if action[0] == 'M':
            print(f'{action[1]} 명의 선교사를 반대편으로 옮깁니다.')
        elif action[0] == 'C':
          print(f'{action[2]} 명의 식인종을 반대편으로 옮깁니다.')
        elif action[0] == 'MC':
          print(f'{abs(action[1])} 명의 선교사와 {abs(action[2])} 명의 식인종을 반대편으로 옮깁니다.')
        elif action[0] == 'S':
         print(f'보트를 반대편으로 보냅니다. (선교사 {start_state["B"]}명, 식인종 {start_state["S"]}명)')
        elif action[0] == 'SC':
         print(f'{abs(action[1])} 명의 선교사와 {abs(action[2])} 명의 식인종을 보트에 태웁니다. (선교사 {start_state["B"] + action[1]}명, 식인종 {start_state["S"] + action[2]}명)')
        start_state = change_state(start_state, action)
 else:
     print('해결할 수 없습니다.')