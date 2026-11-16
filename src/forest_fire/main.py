"""Main of the forest fire model after Drossel and Schwabl"""
# Immediate next step ------------------------------------------------------------------


# Modules importation ------------------------------------------------------------------
import logging as lg
from dataclasses import dataclass
from enum import IntEnum

import numpy as np

# Just for rapid prototyping, will be removed later ------------------------------------
# row = 20
# column = 20
# cycle = 10
p = 0.3
f = 0.1

# Function definition ------------------------------------------------------------------
def enter_int(question: str) -> int:
    """I/O in terminal : Output a question on terminal and await an int from user.
    While no valid int is provided by the user, program will prompt to enter a valid
    int. Does not allow `True` and `False` as int."""
    output = None

    print(question)
    while output is None:
        try:
            output = int(input())
        except (ValueError, TypeError):
            print("Invalid value, enter an integer")
    print("")

    return output

def enter_proba(question: str) -> float:
    """I/O in terminal"""
    output = None

    print(question)
    while output is None:
        try:
            output = float(input())
            if not 0 <= output <= 1:
                output = None
                raise ValueError
        except (ValueError, TypeError):
            print("Invalid value, enter a float between 0 and 1 included")
    print("")

    return output
        

# Class definition ---------------------------------------------------------------------
@dataclass(frozen=True)
class SimParam():
    """Fixed parameters defining the environnment of the simulation."""
    row : int 
    column : int 
    cycles : int 

@dataclass()
class Proba():
    """Variable adjusting probabilities of events occuring"""
    p : float # Probability of a tree growing in an empty space (void)
    f : float # Lightning parameter : probability of a tree catching fire

class State(IntEnum):
    """Values used in the forest fire model to represent a forest."""
    VOID = 0
    TREE = 1
    FIRE = 2

class Matrix:
    """A Class for manipulating a 2d Numpy array as a matrix"""

    def __init__(self, row: int, column: int):
        """Create a 2d NumPy array used as a matrix"""
        # To change for a numpy method ------------------------------
        self.matrix = np.full((row, column), State.VOID, np.uint8)
        
        self.column = column
        self.row = row
        
        temp = np.ones((self.row, self.column), dtype= bool)
        temp[0, :] = False
        self.fix_mask_down = temp.copy()

        temp[:, :] = True
        temp[-1, :] = False
        self.fix_mask_up = np.copy(temp)

        temp[:, :] = True
        temp[:, 0] = False
        self.fix_mask_right = temp.copy()

        temp[:, :] = True
        temp[:, -1] = False
        self.fix_mask_left = np.copy(temp)

    def probabilistic_insert(
            self, 
            probability: float, 
            value_to_replace:int, 
            replacing_value:int
            ):
        """Method for replacing a specific value in the matrix by another value 
        following a given probability."""
        
        if probability == 1:
            self.matrix = np.where(
                self.matrix == value_to_replace, replacing_value, self.matrix
                )
        elif probability == 0:
            pass

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
        """Method for spreading fire to nearby tree while burning down the source fire.
        """
        # Create a truth table of fires in the matrix ----------------------------------
        old_fire_mask = self.matrix == State.FIRE

        # Spread the fire to neighbouring cells ----------------------------------------
        shifted_mask_down = np.roll(old_fire_mask, 1, 0)
        shifted_mask_right = np.roll(old_fire_mask, 1, 1)
        shifted_mask_up = np.roll(old_fire_mask, -1, 0)
        shifted_mask_left = np.roll(old_fire_mask, -1, 1)

        # Remove fires jumping edge to edge --------------------------------------------
        shifted_mask_down = np.logical_and(
            shifted_mask_down, 
            self.fix_mask_down
            )

        shifted_mask_up = np.logical_and(
            shifted_mask_up,
            self.fix_mask_up
            )

        shifted_mask_right = np.logical_and(
            shifted_mask_right, 
            self.fix_mask_right
            )

        shifted_mask_left = np.logical_and(
            shifted_mask_left,
            self.fix_mask_left
        )

        united_mask = np.logical_or(shifted_mask_up, shifted_mask_down)
        united_mask = np.logical_or(united_mask, shifted_mask_left)
        united_mask = np.logical_or(united_mask, shifted_mask_right)

        
        tree_mask = self.matrix == State.TREE
        united_mask = np.logical_and(united_mask, tree_mask)
        
        # Remove old fires -----------------------------------------------------
        self.matrix = np.where(old_fire_mask, State.VOID, self.matrix)

        # Spread fire
        self.matrix = np.where(united_mask, State.FIRE, self.matrix)


    def __str__(self) -> str:
        """Create a human readable string for the matrix"""
        try: 
            return '\n'.join([str(r) for r in self.matrix])
        except(TypeError):
            return str(self.matrix)

# Main function definition -------------------------------------------------------------
def main():
    """Main function of the Drossel forest fire model."""
    # I/O part of the script : defining the parameters of the environnement ------------
    row = enter_int("How many rows do you want in your matrix ?")
    column = enter_int("How many columns do you want in your matrix ?")
    # Will be later replaced by dynamical input control
    cycle = enter_int("How many cycle should the program run for ?")
    lg.info("Terminal input gathered\n")
    # Save of the parameters and creation of the env -----------------------------------
    sim1 = SimParam(row, column, cycle)
    prob1 = Proba(p, f)
    lg.info(f'Simulation parameters collected:\n{sim1}\n\nSimulation probability collected:\n{prob1}\n')

    # Initialisation of the matrix -----------------------------------------------------
    matrix1 = Matrix(sim1.row, sim1.column)
    lg.debug(matrix1)
    matrix1.probabilistic_insert(prob1.p, State.VOID, State.TREE)
    

    # Main loop ------------------------------------------------------------------------
    for n in range(sim1.cycles):
        lg.info(f'Start of cycle {n}')
        print(f'{matrix1}\n')
        matrix1.spread() # Fire spreading
        lg.info(f'Fire spreaded:\n{matrix1}\n')
        matrix1.probabilistic_insert(prob1.f, State.TREE, State.FIRE) # Fire starting
        lg.info(f'Fire lit via lightning:\n{matrix1}\n')
        matrix1.probabilistic_insert(prob1.p, State.VOID, State.TREE) # Tree growing
        lg.info(f'Tree grown:\n{matrix1}\nEnd of the cycle {n}\n')

    lg.info("Program finished")

# Actual running program ---------------------------------------------------------------
if __name__ == "__main__":
    lg.basicConfig(level=lg.WARNING)
    main()
    







    


    
    
    
    
    
    
    
    