"""Main of the forest fire model"""
# Modules importation ------------------------------------------------------------------
import logging
from dataclasses import dataclass


# Function definition ------------------------------------------------------------------
def enter_int(question) -> int:
    """I/O in terminal"""
    output = None

    print(question)
    while output is None:
        try:
            output = int(input())
        except (ValueError, TypeError):
            print("Invalid value")
    print("")

    return output

# Class definition ---------------------------------------------------------------------
@dataclass(frozen=True)
class SimParam():
    row : int 
    column : int 
    cycles : int 

class Matrice:
    def __init__(self, column, row):
        self.matrix = ([[None for w in range(column)] for h in range(row)])

    def repr(self):
        """Create a human readable string for the matrix"""
        return '\n'.join([str(r) for r in self.matrix])

# Main function definition -------------------------------------------------------------
def main():
    
    row = enter_int("How many rows do you want in your matrix ?")
    column = enter_int("How many columns do you want in your matrix ?")
    
    # Will be later replaced by dynamical input control
    cycles = enter_int("How many cycle should the program run for ?")

    sim1 = SimParam(row, column, cycles)
    logging.debug(sim1)
    
    matrix1 = Matrice(sim1.row, sim1.column)
    logging.debug(f'\n{matrix1.repr()}\n')
    
    for n in range(sim1.cycles):
        logging.debug(f'Start of cycle {n}')

# Actual running program ---------------------------------------------------------------
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    main()
    