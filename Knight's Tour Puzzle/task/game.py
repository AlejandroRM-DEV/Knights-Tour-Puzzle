def validate_coords(coords, dimensions):
    if len(coords) != 2:
        return False

    for i in range(0, 2):
        if not coords[i].isdigit():
            return False
        elif int(coords[i]) < 1 or int(coords[i]) > dimensions[i]:
            return False

    return True


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
    def __init__(self, rows, columns):
        self.columns = columns
        self.rows = rows
        self.current_column = None
        self.current_row = None
        self.cell_size = len(str(self.columns * self.rows))
        self.border_length = self.columns * (self.cell_size + 1) + 3
        self.board = [
            ["_" * self.cell_size for _ in range(0, self.columns)]
            for _ in range(0, self.rows)
        ]

    def set_position(self, row,  column, symbol="X"):
        if symbol == "X":
            self.current_column = column
            self.current_row = row

        self.board[row - 1][column - 1] = symbol.rjust(self.cell_size)

    def set_possible_moves(self):
        if self.current_column - 2 >= 1:
            if self.current_row + 1 <= self.rows:
                self.set_position(self.current_row + 1, self.current_column - 2, "O")
            if self.current_row - 1 >= 1:
                self.set_position(self.current_row - 1, self.current_column - 2, "O")

        if self.current_column + 2 <= self.columns:
            if self.current_row + 1 <= self.rows:
                self.set_position(self.current_row + 1, self.current_column + 2, "O")
            if self.current_row - 1 >= 1:
                self.set_position(self.current_row - 1, self.current_column + 2, "O")

        if self.current_row - 2 >= 1:
            if self.current_column + 1 <= self.columns:
                self.set_position(self.current_row - 2, self.current_column + 1, "O")
            if self.current_column - 1 >= 1:
                self.set_position(self.current_row - 2, self.current_column - 1, "O")

        if self.current_row + 2 <= self.rows:
            if self.current_column + 1 <= self.columns:
                self.set_position(self.current_row + 2, self.current_column + 1, "O")
            if self.current_column - 1 >= 1:
                self.set_position(self.current_row + 2, self.current_column - 1, "O")

    def print_board(self):
        print("-" * self.border_length)
        for i in range(len(self.board), 0, -1):
            print(f"{i}| {' '.join(self.board[i - 1])} |")
        print("-" * self.border_length)
        print(f"   {' '.join([str(x).rjust(self.cell_size) for x in range(1, self.columns + 1)])} ")


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

    puzzle = KnightTour(dimensions[1], dimensions[0])

    while True:
        coords = input("Enter the knight's starting position:")
        coords = coords.split(" ")
        if not validate_coords(coords, dimensions):
            print("Invalid position!")
        else:
            coords = list(map(int, coords))
            break

    puzzle.set_position(coords[1], coords[0])
    puzzle.set_possible_moves()
    puzzle.print_board()
