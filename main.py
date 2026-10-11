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
def create_matrix(height: int, width: int):
    return ([[None for w in range(width)] for h in range(height)])

def enter_matrix_size() -> tuple[int, int]:
    "IO call, return height and width"
    row = None
    column = None

    print("How many rows do you want in your matrix ?")
    while row is None:
        try:
            row = int(input())
        except (ValueError, TypeError):
            print("invalid value")
    print('')

    print("How many columns do you want in your matrix ?")
    while column is None:
        try:
            column = int(input())
        except (ValueError, TypeError):
            print("invalid value")
    print('')

    return row, column

def matrix_as_str(matrix: list[list]) -> str:
    mstring = '\n'.join([str(r) for r in matrix])
    # for r in matrix:
    #     mstring += str(r)
    #     mstring += '\n'
    logging.debug('\n' + mstring)
    return mstring
    

# Main function definition -------------------------------------------------------------
def main():
    row, column = enter_matrix_size()
    matrix = create_matrix(row, column)
    matrix_as_str(matrix)

    logging.info

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()
    # test_list = [[], []]
    # print(str(test_list))