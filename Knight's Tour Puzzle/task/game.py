def validate_dimensions(dimensions):
    if len(dimensions) != 2:
        return False

    for n in dimensions:
        if not n.isdigit():
            return False
        elif int(n) < 1:
            return False

    return True


class KnightTour:
    def __init__(self, columns, rows):
        self.moves = 0
        self.columns = columns
        self.rows = rows
        self.current_column = None
        self.current_row = None
        self.total_cells = columns * rows
        self.cell_size = len(str(self.columns * self.rows))
        self.border_length = self.columns * (self.cell_size + 1) + 3
        self.board = [
            ["_" * self.cell_size for _ in range(0, self.columns)]
            for _ in range(0, self.rows)
        ]
        self.move_col = [-2, -2, 2, 2, 1, -1, 1, -1]
        self.move_row = [1, -1, 1, -1, -2, -2, 2, 2]

    def reset(self):
        self.moves = 0
        self.board = [
            ["_" * self.cell_size for _ in range(0, self.columns)]
            for _ in range(0, self.rows)
        ]

    def set_position(self, column, row,  symbol="X"):
        if symbol == "X":
            if self.current_column:
                self.board[self.current_row-1][self.current_column-1] = "*".rjust(self.cell_size)

            self.current_column = column
            self.current_row = row
            self.moves += 1

            for i in range(self.rows):
                for j in range(self.columns):
                    if self.board[i][j].strip().isdigit():
                        self.board[i][j] = "_" * self.cell_size

        self.board[row - 1][column - 1] = symbol.rjust(self.cell_size)

    def set_possible_moves(self):
        def explore_moves(col, row):
            if col < 1 or col > self.columns or row < 1 or row > self.rows or self.board[row-1][col-1].strip() == "*":
                return

            self.set_position(col, row, str(self.count_possible_move(col, row)))

        explore_moves(self.current_column - 2, self.current_row + 1)
        explore_moves(self.current_column - 2, self.current_row - 1)
        explore_moves(self.current_column + 2, self.current_row + 1)
        explore_moves(self.current_column + 2, self.current_row - 1)
        explore_moves(self.current_column + 1, self.current_row - 2)
        explore_moves(self.current_column - 1, self.current_row - 2)
        explore_moves(self.current_column + 1, self.current_row + 2)
        explore_moves(self.current_column - 1, self.current_row + 2)

    def count_possible_move(self, column, row):
        def count_moves_recursive(col, rw):
            if (col < 1 or col > self.columns or rw < 1 or rw > self.rows or
                    self.board[rw-1][col-1].strip() == "X" or
                    self.board[rw-1][col-1].strip() == "*"):
                return 0
            else:
                return 1

        moves = 0
        moves += count_moves_recursive(column - 2, row + 1)
        moves += count_moves_recursive(column - 2, row - 1)
        moves += count_moves_recursive(column + 2, row + 1)
        moves += count_moves_recursive(column + 2, row - 1)
        moves += count_moves_recursive(column + 1, row - 2)
        moves += count_moves_recursive(column - 1, row - 2)
        moves += count_moves_recursive(column + 1, row + 2)
        moves += count_moves_recursive(column - 1, row + 2)

        return moves

    def print_board(self):
        print("-" * self.border_length)
        for i in range(len(self.board), 0, -1):
            print(f"{i}| {' '.join(self.board[i - 1])} |")
        print("-" * self.border_length)
        print(f"   {' '.join([str(x).rjust(self.cell_size) for x in range(1, self.columns + 1)])} ")

    def validate_coords(self, coords):
        dimensions = [self.columns, self.rows]
        if len(coords) != 2:
            return False

        for i in range(0, 2):
            if not str(coords[i]).isdigit():
                return False
            elif coords[i] < 1 or coords[i] > dimensions[i]:
                return False

        if (self.board[coords[1]-1][coords[0]-1].strip() == "X" or
                self.board[coords[1]-1][coords[0]-1].strip() == "*"):
            return False

        return True

    def has_more_moves(self):
        return self.count_possible_move(self.current_column, self.current_row) > 0
    
    def is_l_move(self, coords):
        col_diff = abs(coords[0] - self.current_column)
        row_diff = abs(coords[1] - self.current_row)
        return (col_diff == 1 and row_diff == 2) or (col_diff == 2 and row_diff == 1)

    def has_won(self):
        return self.moves == self.total_cells

    def solution(self, row, col, move_count):
        if move_count == self.columns * self.rows:
            return True
        for i in range(8):
            next_row = row + self.move_row[i]
            next_col = col + self.move_col[i]
            if (0 <= next_col < self.columns and 0 <= next_row < self.rows and
                    not self.board[next_row][next_col].strip().isdigit()):
                self.board[next_row][next_col] = str(move_count + 1).rjust(self.cell_size)
                if self.solution(next_row, next_col, move_count + 1):
                    return True
                self.board[next_row][next_col] = "_" * self.cell_size

        return False

    def find_solution(self):
        self.board[self.current_row-1][self.current_column-1] = "1".rjust(self.cell_size)
        return self.solution(self.current_row-1, self.current_column-1, 1)


if __name__ == "__main__":
    dimensions = None
    coords = None

    while True:
        dimensions = input("Enter your board dimensions:")
        dimensions = dimensions.split(" ")
        if not validate_dimensions(dimensions):
            print("Invalid dimensions!")
        else:
            dimensions = list(map(int, dimensions))
            break

    puzzle = KnightTour(dimensions[0], dimensions[1])

    while True:
        try:
            coords = input("Enter the knight's starting position:")
            coords = coords.split(" ")
            coords = list(map(int, coords))
            if not puzzle.validate_coords(coords):
                raise Exception
            else:
                break
        except:
            print("Invalid position!")

    puzzle.set_position(coords[0], coords[1])

    while True:
        want_try = input("Do you want to try the puzzle? (y/n):")
        if want_try == "y":
            if puzzle.find_solution():
                puzzle.reset()
                puzzle.set_position(coords[0], coords[1])
            else:
                print("No solution exists!")
                break

            while puzzle.has_more_moves():
                while True:
                    try:
                        coords = input("Enter your next move:")
                        coords = coords.split(" ")
                        coords = list(map(int, coords))
                        if not puzzle.validate_coords(coords) or not puzzle.is_l_move(coords):
                            print("Invalid move!", end="")
                        else:
                            break
                    except:
                        print("Invalid move!")

                puzzle.set_position(coords[0], coords[1])
                puzzle.set_possible_moves()
                puzzle.print_board()

            if puzzle.has_won():
                print("What a great tour! Congratulations!")
            else:
                print("No more possible moves!")
                print(f"Your knight visited {puzzle.moves} squares!")
            break

        elif want_try == "n":
            if puzzle.find_solution():
                print("Here's the solution!")
                puzzle.print_board()
            else:
                print("No solution exists!")
            break

        else:
            print("Invalid input!")
