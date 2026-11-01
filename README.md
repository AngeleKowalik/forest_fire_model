# Forest fire model
## Goal 
Recreating the forest fire model after Drossel and Schwabl work. The goal is to see if the same results can be gathered with this script.

It is caracterized by four rules : 
- A burning cell turns into an empty cell
- A tree will burn if at least one neighbour is burning
- A tree will ignite with probability $f$ even if no neighbour is burning
- An empty space fill with a tree with probability $p$

## Project structure
The project is centered around a matrix created from a NumPy array for efficency as it use C for computation. At the startup, this array is entirely filled with 0s reprensenting void. Then, the main loop is executed. With each iterations :
- Trees grow randomly on void's spots following the probability $p$
- Fire is lighten up replacing random trees following the probability $f$
- If there is adjacent trees near a fire, the fire burn out and is replaced by void while it spread to nearby trees.

The backbone and computation logic of the program is entirely separated from the I/O part so future implementation will be able to make it run quickly without animations to gather pure data.

## Roadmap
- [ ] Implementing a safeguard system to protect from wrong hard coded values (using IntNum)
- [ ] Writing a function for the user to enter float between 0 and 1 (for proba)
- [ ] Implementing graphs using Matplotlib
- [ ] Creating tests using pytest for each functions
- [ ] Adding a visualisation using pygame or similar library
- [ ] Storing results of each runs in an outside file

## Fixes to make
- [x] Checking original paper to see the correct order of operation
- [x] Refactoring the spreading function to remove fire jumping from side to side of the matrix bug
- [ ] Improving the slow python's loops by using NumPy methods instead





