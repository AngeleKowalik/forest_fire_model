# Forest fire model
## Goal 
Recreating the forest fire model after Drossel and Schwabl work. 

It is caracterized by four rules : 
- A burning cell turns into an empty cell
- A tree will burn if at least one neighbour is burning
- A tree will ignite with probability $f$ even if no neighbour is burning
- An empty space fill with a tree with probability $p$

## Project structure
Define a class for a tree and a class for a fire

- Initialise an empty grid of n*n
- Each tick, if space is empty then possibility to spawn a tree $p$
- If tree possibility to spawn a fire $f$
- If fire and tree contingent, then fire spread and parent fire die
- 


