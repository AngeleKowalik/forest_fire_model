"""Main of the forest fire model"""
# Modules importation ------------------------------------------------------------------
import logging


# Class definition ---------------------------------------------------------------------
class Tree:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Fire:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def spread(self):
        raise NotImplementedError

    def die(self):
        raise NotImplementedError

# Function definition ------------------------------------------------------------------
def create_matrice(height: int, width: int):
    return ([[None for w in range(width)] for h in range(height)])

def enter_matrice_size() -> tuple[int, int]:
    "IO call, return height and width"
    row = None
    column = None

    print("How many rows do you want in your matrice ?")
    while row is None:
        try:
            row = int(input())
        except (ValueError, TypeError):
            print("invalid value")

    print("How many columns do you want in your matrice ?")
    while column is None:
        try:
            column = int(input())
        except (ValueError, TypeError):
            print("invalid value")

    return row, column

def print_matrice(matrice):
    for row in matrice:
        print(row)

# Main function definition -------------------------------------------------------------
def main():
    row, column = enter_matrice_size()
    matrice = create_matrice(row, column)
    logging.debug(print_matrice(matrice))


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()