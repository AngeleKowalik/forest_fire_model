"""Main of the forest fire model"""
# Next steps list ----------------------------------------------------------------------
# - Create a system to store informations from the program
# - Implement testing for each function
# - Implement a safeguard for wrong input (outside of State(IntEnum))
# - Implement graph using matplotlib


# Modules importation ------------------------------------------------------------------
import logging as lg
from dataclasses import dataclass
from enum import IntEnum

import numpy as np

row = 20
column = 20
cycle = 10
p = 0.3
f = 0.1

# Function definition ------------------------------------------------------------------
def enter_int(question: str) -> int:
    """I/O in terminal"""
    output = None

    print(question)
    while output is None:
        try:
            output = int(input())
        except (ValueError, TypeError):
            print("Invalid value, enter an integer")
    print("")

    return output

# Class definition ---------------------------------------------------------------------
@dataclass(frozen=True)
class SimParam():
    """Fixed parameters defining the environnment of the simulation"""
    row : int 
    column : int 
    cycles : int 

@dataclass()
class Proba():
    p : float # Probability of a tree growing in an empty space (void)
    f : float # Lightning parameter : probability of a tree catching fire

class State(IntEnum):
    VOID = 0
    TREE = 1
    FIRE = 2

class Matrix:
    """Create a 2d list used as a matrix"""
    def __init__(self, column: int, row: int):
        self.matrix = np.array(
            [[State.VOID for c in range(column)] for r in range(row)], 
            dtype=np.uint8
            )
        self.column = column
        self.row = row

    def probabilistic_insert(self, probability: float, value_to_replace, replacing_value):
        if isinstance(probability, int):
            self.matrix = np.where(
                self.matrix == value_to_replace, replacing_value, self.matrix
                )

        else:
            condition_list = np.random.uniform(0, 1,(self.row, self.column))
            
            self.matrix = np.where(
                # Using the bitwise operator because comparing two arrays of boolean 
                # values
                # with `and` is not possible as `and` only compare one value and not an
                # array while bitwise operators compare bit by bit
                (self.matrix == value_to_replace) & (condition_list <= probability), 
                replacing_value, 
                self.matrix
                )

    def spread(self):
        # Part to fix
        row, column = -1, -1
        coordinate_list = []
        for r in self.matrix:
            row += 1
            for c in r:
                column += 1
                if c == State.FIRE:
                    coordinate_list.append([row, column])
            column = -1

        # Fixed part
        

        coordinate_to_change = []
        for coordinate in coordinate_list:
            coordinate_to_change.append(
                [
                    [coordinate[0] - 1, coordinate[1]], 
                    [coordinate[0] + 1, coordinate[1]],
                    [coordinate[0], coordinate[1] - 1],
                    [coordinate[0], coordinate[1] + 1]
                ]
                )

        for coordinate in coordinate_to_change:
            for c in coordinate:
                try:
                    if self.matrix[c[0], c[1]] == State.TREE:
                        self.matrix[c[0], c[1]] = State.FIRE
                except IndexError:
                    pass

        for coordinate in coordinate_list:
            self.matrix[coordinate[0], coordinate[1]] = State.VOID



    def repr(self) -> str:
        """Create a human readable string for the matrix"""
        try: 
            return '\n'.join([str(r) for r in self.matrix])
        except(TypeError):
            return str(self.matrix)

# Main function definition -------------------------------------------------------------
def main():
    # I/O part of the script : defining the parameters of the environnement ------------
    # row = enter_int("How many rows do you want in your matrix ?")
    # column = enter_int("How many columns do you want in your matrix ?")
    # # Will be later replaced by dynamical input control
    # cycle = enter_int("How many cycle should the program run for ?")

    # Save of the parameters and creation of the env -----------------------------------
    sim1 = SimParam(row, column, cycle)
    prob1 = Proba(p, f)
    lg.debug(sim1)

    # Initialisation of the matrix -----------------------------------------------------
    matrix1 = Matrix(sim1.column, sim1.row)
    lg.debug(f'\n{matrix1.repr()}\n')
    matrix1.probabilistic_insert(prob1.p, State.VOID, State.TREE)
    lg.debug("\n" + matrix1.repr() + "\n")
    

    # Main loop ------------------------------------------------------------------------
    for n in range(sim1.cycles):
        lg.info(f'Start of cycle {n}')
        lg.debug(f'\n{matrix1.repr()}\n')
        matrix1.probabilistic_insert(prob1.p, State.VOID, State.TREE) # Tree growing
        matrix1.spread() # Fire spreading
        matrix1.probabilistic_insert(prob1.f, State.TREE, State.FIRE) # Fire starting

        

def test_function():
    matrix1 = Matrix(10, 5)
    lg.debug(f'cycle 1 : \n{matrix1.repr()}\n')
    matrix1.probabilistic_insert(p, State.VOID, State.TREE)
    lg.debug(f'cycle 2 : \n{matrix1.repr()}')
    sim1 = SimParam(10, 5, 1)
    matrix1.matrix[2][4] = 2

    lg.debug(f'cycle 3 : introduction of the fire\n{matrix1.repr()}')
    
    
    # Test spread ----------------------------------------------------------------------

    spread()
    lg.debug(f'cycle 4 : Spreading the fire\n{matrix1.repr()}')
    spread()
    lg.debug(f'cycle 5 : Spreading the fire\n{matrix1.repr()}')
    spread()
    lg.debug(f'cycle 5 : Spreading the fire\n{matrix1.repr()}')

    
    
            

        

    # print(coordinate_list)

# Actual running program ---------------------------------------------------------------
if __name__ == "__main__":
    lg.basicConfig(level=lg.DEBUG)
    main()
    # test_function()

    

    
    
    
    
    