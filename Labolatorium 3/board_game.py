import random
import sys


def generate_board():
    board = [['_' for _ in range(5)] for _ in range(5)]

    start_row = random.randint(0, 4)
    start_col = random.choice([0, 4])
    board[start_row][start_col] = 'S'

    end_row = random.choice([0, 4])
    end_col = random.randint(0, 4)
    while board[end_row][end_col] != '_':
        end_row = random.choice([0, 4])
        end_col = random.randint(0, 4)
    board[end_row][end_col] = 'E'

    obstacles = 0
    while obstacles < 3:
        obstacle_row = random.randint(0, 4)
        obstacle_col = random.randint(0, 4)
        if board[obstacle_row][obstacle_col] == '_':
            board[obstacle_row][obstacle_col] = 'X'
            obstacles += 1

    return board, start_row, start_col, end_row, end_col


def print_board(board):
    for row in board:
        print(' '.join(row))


def move_player(board, direction, current_row, current_col, start_row, start_col):
    new_row, new_col = current_row, current_col

    if direction == 'w' and current_row > 0:
        new_row -= 1
    elif direction == 's' and current_row < len(board) - 1:
        new_row += 1
    elif direction == 'a' and current_col > 0:
        new_col -= 1
    elif direction == 'd' and current_col < len(board[0]) - 1:
        new_col += 1

    if board[new_row][new_col] != 'X':
        if board[new_row][new_col] != 'E':
            board[current_row][current_col] = '_'
        else:
            board[current_row][current_col] = 'E'
        board[new_row][new_col] = '#'
        return new_row, new_col, start_row, start_col
    else:
        print("You cannot move there. There is an obstacle!")
        return current_row, current_col, start_row, start_col  # Player stays in the current position


def main():
    game_board, player_row, player_col, end_row, end_col = generate_board()

    start_row, start_col = player_row, player_col

    while True:
        print("\nCurrent board:")
        print_board(game_board)
        move = input("Enter the direction (W - up, S - down, A - left, D - right): ").lower()

        if move in ['w', 's', 'a', 'd']:
            player_row, player_col, start_row, start_col = move_player(game_board, move, player_row, player_col,
                                                                       start_row, start_col)
            if player_row == end_row and player_col == end_col:
                game_board[player_row][player_col] = '#'
                print("\nCurrent board:")
                print_board(game_board)
                print("Congratulations! You've reached the end point!")
                break
            else:
                game_board[start_row][start_col] = 'S'
        else:
            print("Invalid direction. Please enter a valid move.")


if __name__ == "__main__":
    main()
