def validate(coords):
    if len(coords) != 2:
        return False

    for n in coords:
        if not n.isdigit():
            return False
        elif int(n) < 1 or int(n) > 8:
            return False

    return True


if __name__ == "__main__":
    coords = input("Enter the knight's starting position:")
    coords = coords.split(" ")

    if not validate(coords):
        print("Invalid dimensions!")
        exit()

    coords = list(map(int, coords))
    board = [["_" for _ in range(0, 8)] for _ in range(0, 8)]
    board[coords[1] - 1][coords[0] - 1] = "X"
    print(" -------------------")
    print("8| " + " ".join(board[7]) + " |")
    print("7| " + " ".join(board[6]) + " |")
    print("6| " + " ".join(board[5]) + " |")
    print("5| " + " ".join(board[4]) + " |")
    print("4| " + " ".join(board[3]) + " |")
    print("3| " + " ".join(board[2]) + " |")
    print("2| " + " ".join(board[1]) + " |")
    print("1| " + " ".join(board[0]) + " |")
    print(" -------------------")
    print("   1 2 3 4 5 6 7 8 ")
