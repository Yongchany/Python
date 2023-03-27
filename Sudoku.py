import numpy as np

def create_board():
    # 9x9 스도쿠 게임판을 생성하는 함수
    board = np.zeros((9, 9), dtype=int)
    return board

def print_board(board):
    # 스도쿠 게임판을 출력하는 함수
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")
                
def find_empty(board):
    # 스도쿠 게임판에서 빈 칸을 찾는 함수
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # 빈 칸의 행과 열을 반환
    return None  # 빈 칸이 없으면 None을 반환

def is_valid(board, num, pos):
    # 스도쿠 게임판에서 숫자가 유효한지 확인하는 함수
    # 행에서 확인
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # 열에서 확인
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # 3x3 박스에서 확인
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True  # 숫자가 유효하면 True를 반환

def solve_board(board):
    # 스도쿠 게임판을 풀기 위한 재귀 함수
    empty = find_empty(board)
    if not empty:
        return True  # 모든 칸이 채워졌으면 스도쿠 퍼즐이 풀린 것

    row, col = empty

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve_board(board):
                return True

            board[row][col] = 0

    return False  # 스도쿠 퍼즐을 풀 수 없는 경우 False를 반환

def is_board_complete(board):
    # 스도쿠 게임판이 완성되었는지 확인하는 함수
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return False
    return True

def is_valid_move(board, row, col, value):
    # 사용자가 입력한 값이 유효한지 확인하는 함수
    # 행에서 확인
    for i in range(len(board[0])):
        if board[row][i] == value and col != i:
            return False

    # 열에서 확인
    for i in range(len(board)):
        if board[i][col] == value and row != i:
            return False

    # 3x3 박스에서 확인
    box_x = col // 3
    box_y = row // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == value and (i, j) != (row, col):
                return False

    return True  # 값이 유효하면 True를 반환

def play_game():
    board = create_board()
    print("Welcome to Sudoku game!\n")
    print_board(board)
    print("\nTo play the game, please enter the row and column numbers of the cell you want to fill (separated by space), and then enter the value you want to put in that cell.\n")
    while not is_board_complete(board):
        row, col, value = input("Enter row, column, and value (e.g. '1 2 3'): ").split()
        row = int(row) - 1
        col = int(col) - 1
        value = int(value)
        if is_valid_move(board, row, col, value):
            board[row][col] = value
            print_board(board)
            print()
        else:
            print("Invalid move! Please try again.\n")
    print("Congratulations! You solved the puzzle.")

play_game()