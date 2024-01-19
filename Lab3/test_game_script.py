import unittest
from io import StringIO
from unittest.mock import patch
from board_game import generate_board, print_board, move_player

class TestGame(unittest.TestCase):

    def test_invalid_input(self):
        game_board, player_row, player_col, _, _ = generate_board()

        with patch('builtins.input', return_value='q'), patch('sys.stdout', new=StringIO()) as fake_out:
            move_player(game_board, 'q', player_row, player_col, player_row, player_col)
            expected_output = "Invalid direction. Please enter a valid move."
            output = fake_out.getvalue()

            print("Expected Output:", expected_output)
            print("Actual Output:", output)

            self.assertIn(output, expected_output, "Invalid input message not displayed")

    def test_valid_input(self):
        game_board, player_row, player_col, _, _ = generate_board()

        with patch('builtins.input', side_effect=['w']):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                move_player(game_board, 'w', player_row, player_col, player_row, player_col)
                expected_output = ""

                self.assertNotIn("Invalid direction", fake_out.getvalue(), "No output should contain an invalid input message")

    def test_start_point_on_edge(self):
        _, start_row, start_col, _, _ = generate_board()
        board_size = 5

        is_on_edge = start_row == 0 or start_row == board_size - 1 or start_col == 0 or start_col == board_size - 1
        self.assertTrue(is_on_edge, "The starting point 'S' should be on the edge of the board")

    def test_end_point_on_edge(self):
        _, _, _, end_row, end_col = generate_board()
        board_size = 5

        is_on_edge = end_row == 0 or end_row == board_size - 1 or end_col == 0 or end_col == board_size - 1
        self.assertTrue(is_on_edge, "The end point 'E' should be on the edge of the board")

    def test_player_movement_boundaries(self):
        board_size = 5
        game_board, _, _, _, _ = generate_board()
        print("Test: test_player_movement_boundaries")

        # Test top edge
        target_row_top = 0
        for col_top in range(board_size - 1):
            if game_board[target_row_top][col_top] == '_':
                new_row_top, new_col_top, _, _ = move_player(game_board, 'w', target_row_top, col_top, target_row_top,
                                                             col_top)
                print_board(game_board)
                self.assertEqual(new_col_top, col_top,
                                 "The player should not be able to move beyond the top edge of the board")
                break

        # Test bottom edge
        target_row_bottom = 4
        for col_bottom in range(board_size - 1):
            if game_board[target_row_bottom][col_bottom] == '_':
                new_row_bottom, new_col_bottom, _, _ = move_player(game_board, 's', target_row_bottom, col_bottom,
                                                                   target_row_bottom, col_bottom)
                print_board(game_board)
                self.assertEqual(new_col_bottom, col_bottom,
                                 "The player should not be able to move beyond the bottom edge of the board")
                break

        # Test left edge
        target_col_left = 0
        for row_left in range(board_size - 1):
            if game_board[target_col_left][row_left] == '_':
                new_row_left, new_col_left, _, _ = move_player(game_board, 'a', row_left, target_col_left, row_left,
                                                               target_col_left)
                print_board(game_board)
                self.assertEqual(new_row_left, row_left,
                                 "The player should not be able to move beyond the left edge of the board")
                break

        # Test right edge
        target_col_right = 4
        for row_right in range(board_size - 1):
            if game_board[target_col_right][row_right] == '_':
                new_row_right, new_col_right, _, _ = move_player(game_board, 'd', row_right, target_col_right,
                                                                 row_right, target_col_right)
                print_board(game_board)
                self.assertEqual(new_row_right, row_right,
                                 "The player should not be able to move beyond the right edge of the board")
                break

    def test_invalid_movement_direction(self):
        game_board, player_row, player_col, _, _ = generate_board()

        new_row, new_col = move_player(game_board, 'x', player_row, player_col, player_row, player_col)[0:2]
        self.assertEqual((new_row, new_col), (player_row, player_col), "An invalid movement direction should not change the player's position")

    def test_movement_without_obstacles(self):
        board_size = 5
        game_board, _, _, _, _ = generate_board()
        print("Test: test_movement_without_obstacles")

        # Set up initial player position
        player_row, player_col = 2, 2
        game_board[player_row][player_col] = '_'

        # Create an open space around the player
        for row_offset in range(-1, 2):
            for col_offset in range(-1, 2):
                new_row = player_row + row_offset
                new_col = player_col + col_offset
                if 0 <= new_row < board_size and 0 <= new_col < board_size:
                    game_board[new_row][new_col] = '_'

        # Test movement up
        new_row, new_col = move_player(game_board, 'w', player_row, player_col, player_row, player_col)[:2]
        self.assertEqual((new_row, new_col), (player_row - 1, player_col), "The player should be able to move up")

        # Test movement down
        new_row, new_col = move_player(game_board, 's', player_row, player_col, player_row, player_col)[:2]
        self.assertEqual((new_row, new_col), (player_row + 1, player_col), "The player should be able to move down")

        # Test movement left
        new_row, new_col = move_player(game_board, 'a', player_row, player_col, player_row, player_col)[:2]
        self.assertEqual((new_row, new_col), (player_row, player_col - 1), "The player should be able to move left")

        # Test movement right
        new_row, new_col = move_player(game_board, 'd', player_row, player_col, player_row, player_col)[:2]
        self.assertEqual((new_row, new_col), (player_row, player_col + 1), "The player should be able to move right")

        def test_collision_message(self):
            game_board, player_row, player_col, _, _ = generate_board()

            with patch('sys.stdout', new=StringIO()) as fake_out:
                while True:
                    next_row = player_row + 1
                    next_col = player_col
                    if next_row < len(game_board) and game_board[next_row][next_col] != 'X':
                        game_board[next_row][next_col] = 'X'
                        break
                    else:
                        player_row = (player_row + 1) % len(game_board)

                original_board_str = '\n'.join([' '.join(row) for row in game_board])

                move_player(game_board, 's', player_row, player_col, player_row, player_col)
                expected_output = "You cannot move there. There is an obstacle!\n"

                self.assertEqual(fake_out.getvalue(), expected_output,
                                 "Collision message with obstacle was not displayed")

                updated_board_str = '\n'.join([' '.join(row) for row in game_board])
                self.assertEqual(updated_board_str, original_board_str,
                                 "The board was modified after a collision with an obstacle")


if __name__ == "__main__":
    unittest.main()
