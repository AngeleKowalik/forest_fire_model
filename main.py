"""Main of the forest fire model"""
# Modules importation ------------------------------------------------------------------
import logging as lg
from dataclasses import dataclass
from enum import IntEnum
import random

import numpy as np


# Function definition ------------------------------------------------------------------
def enter_int(question) -> int:
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

# To do
# Create a paramater to pass the actual argument to be filled with
# Let a probabilistic repartition be defined


class Matrix:
    """Create a 2d list used as a matrix"""
    def __init__(self, column, row):
        self.matrix = np.array(
            [[State.VOID for c in range(column)] for r in range(row)], 
            dtype=np.uint8
            )

    def probabilistic_insert(self, probability, value_to_replace, replacing_value):
        self.matrix = np.array(
            [[replacing_value 
              if random.uniform(0, 1) <= probability 
              and column == value_to_replace 
              else column for column in row] 
             for row in self.matrix])

        # np.where()

    def repr(self) -> str:
        """Create a human readable string for the matrix"""
        return '\n'.join([str(r) for r in self.matrix])

# Main function definition -------------------------------------------------------------
def main():
    # I/O part of the script : defining the parameters of the environnement ------------
    row = enter_int("How many rows do you want in your matrix ?")
    column = enter_int("How many columns do you want in your matrix ?")
    # Will be later replaced by dynamical input control
    cycles = enter_int("How many cycle should the program run for ?")

    # Save of the parameters and creation of the env -----------------------------------
    sim1 = SimParam(row, column, cycles)
    lg.debug(sim1)
    
    matrix1 = Matrix(sim1.column, sim1.row)
    lg.debug(f'\n{matrix1.repr()}\n')

    matrix1.probabilistic_insert(0.2, 0, 1)
    lg.debug(matrix1.repr())
    

    # Main loop ------------------------------------------------------------------------
    for n in range(sim1.cycles):
        lg.debug(f'Start of cycle {n}')

def test_function():
    matrix1 = Matrix(10, 5)
    matrix1.probabilistic_insert(0.3, 0, 1)
    print(matrix1.repr())
    
# Actual running program ---------------------------------------------------------------
if __name__ == "__main__":
    lg.basicConfig(level=lg.DEBUG)
    # main()
    test_function()

    

    
    
    
    
    