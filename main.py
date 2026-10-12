"""Main of the forest fire model"""
# Modules importation ------------------------------------------------------------------
import logging


# Function definition ------------------------------------------------------------------
def create_matrix(height: int, width: int) -> list[list[None]]:
    """Create a matrix as a 2D list"""
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
    return mstring

def enter_simulation_length() -> int:
    cycles = None
    
    print("How many cycle should the program run for ?")
    while cycles is None:
        try:
            cycles = int(input())
        except (ValueError, TypeError):
            print("invalid value")
    print('')

    return cycles

# Main function definition -------------------------------------------------------------
def main():
    row, column = enter_matrix_size()
    matrix = create_matrix(row, column)
    matrice_string = matrix_as_str(matrix)
    logging.debug('\n' + matrice_string + '\n')

    # Will be later replaced by dynamical input control
    cycles = enter_simulation_length()
    for n in range(cycles):
        print('ok')

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()
    