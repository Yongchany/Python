def is_goal_state(state):
    pass


def apply_action(state, action):
    pass


def main():
    # Define the starting state
    state = {'M': 3, 'C': 3, 'B': 1, 'S': 0}

    # Print the instructions
    print('선교사와 식인종 게임')
    print('==============================')
    print('세 선교사와 세 식인종이 강을 건너려고 합니다.')
    print('보트는 한번에 두명까지 탑승할 수 있습니다.')
    print('선교사보다 식인종이 많다면, 선교사는 잡아먹힐 겁니다.')
    print('모두가 안전하게 강을 건너야 합니다.')

    # Print the initial state
    print_state(state)

    # Start the game loop
    while not is_goal_state(state):
        # Get the next move from the player
        action = get_action()

        # Apply the action to the current state
        new_state = apply_action(state, action)
        if new_state is None:
            print('다시 입력하세요. 불가능한 움직임입니다.')
            continue

        # Update the state and print it
        state = new_state
        print_state(state)

    # Print the final message
    print('축하합니다! 모두가 강을 안전하게 건넜습니다.')

# Define a function to print the current state
def print_state(state):
    print('==============================')
    print('M: ' + 'M'*state['M'] + '  C: ' + 'C'*state['C'] + '  B: ' + 'B'*state['B'] + '  S: ' + 'S'*state['S'])
    print('==============================')

# Define a function to get the player's next move
def get_action():
    while True:
        action_str = input('다음 움직임을 입력하세요. (예시: "M2C1" 2명의 선교사와 1명의 식인종을 움직인다): ')
        if len(action_str) != 3 or action_str[0] not in ('M', 'C') or action_str[1] not in ('1', '2') or action_str[2] not in ('1', '2'):
            print('불가능한 움직임입니다! 다음과 같은 형식으로 움직임을 입력하세요. "M2C1".')
            continue
        action = (action_str[0], int(action_str[1])*(-1 if action_str[0] == 'M' else 1), int(action_str[2])*(-1 if action_str[0] == 'C' else 1))
        return action

# Call the main function
if __name__ == '__main__':
    main()
