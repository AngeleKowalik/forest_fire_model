# Forest fire model
## Goal 
Recreating the forest fire model after Drossel and Schwabl work. 

It is caracterized by four rules : 
- A burning cell turns into an empty cell
- A tree will burn if at least one neighbour is burning
- A tree will ignite with probability $f$ even if no neighbour is burning
- An empty space fill with a tree with probability $p$


