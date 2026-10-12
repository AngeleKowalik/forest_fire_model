"""Main of the forest fire model"""
# Modules importation ------------------------------------------------------------------
import logging


# Function definition ------------------------------------------------------------------
def create_matrix(height: int, width: int) -> list[list[None]]:
    """Create a matrix as a 2D list"""
    return ([[None for w in range(width)] for h in range(height)])

def matrix_as_str(matrix: list[list]) -> str:
    mstring = '\n'.join([str(r) for r in matrix])
    return mstring

def enter_int(question) -> int:
    output = None

    print(question)
    while output is None:
        try:
            output = int(input())
        except (ValueError, TypeError):
            print("Invalid value")
    print("")

    return output

# Main function definition -------------------------------------------------------------
def main():
    row = enter_int("How many rows do you want in your matrix ?")
    column = enter_int("How many columns do you want in your matrix ?")
    matrix = create_matrix(row, column)
    matrice_string = matrix_as_str(matrix)
    logging.debug('\n' + matrice_string + '\n')

    # Will be later replaced by dynamical input control
    cycles = enter_int("How many cycle should the program run for ?")
    for n in range(cycles):
        print('ok')

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()
    