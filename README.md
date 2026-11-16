# Forest fire model
[Lien vers la documentation française](README_FR.md) | [Skip to installation](#installation)

This project is an implementation of the Drossel and Schwabl forest-fire model from 1992. It is one of the earliest cellular automata dedicated to studying self-organized criticality. 

It operates on a 2D matrix populated with trees, void or fire. The fire spreads to nearby trees while source fire dies out. This mechanism allow for an emergent power-law distribution of burned forest clusters and self-organized criticality.

This version is entirely built in Python using NumPy vectorization to improve efficiency by running C under the hood. It features strict type-hinting, logging and testing to ensure long-term maintainability.

## Table of contents
- [Scientific references](#scientific-references)
- [Model architecture](#model-architecture)
    - [Lattice settings](#lattice-settings)
    - [Update rules](#update-rules)
- [Software architecture](#software-architecture)
    - [Vectorized Numpy](#vectorized-numpy)
    - [Code quality](#code-quality)
    - [Repository structure](#repository-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
    - [Explanation](#explanation)
    - [Execution](#execution)
- [Roadmap](#roadmap)
- [Fixes to make](#fixes-to-make)

## Scientific references
This implementation relies heavily upon these papers:
* **Foundational model:** P. Bak, K. Chen, and C. Tang, *"A forest-fire model and some thoughts on turbulence"*, Physics Letters A, vol. 147, no. 5–6, pp. 297–300, 1990. DOI: [10.1016/0375-9601(90)90451-S](https://doi.org/10.1016/0375-9601(90)90451-S)
* **Self-organized critical extension (implemented here):** B. Drossel and F. Schwabl, *"Self-organized critical forest-fire model"*, Physical Review Letters, vol. 69, no. 11, pp. 1629–1632, 1992. DOI: [10.1103/PhysRevLett.69.1629](https://doi.org/10.1103/PhysRevLett.69.1629)

The first model emulates a fractal distribution of energy dissipation in a closed system, but it has a major flaw: fire needs to be introduced manually and reignited as it will eventually die out.

The second model demonstrates self-organized criticality, with the system naturally evolving toward a power-law distribution of burned clusters when lightning frequency (probability of a tree igniting) is much smaller than tree growth ($f \ll p \ll 1$).

## Model architecture
### Lattice settings
The automaton's lattice is a discrete 2D grid of dimensions $R \times C$ ($row \times column$). Its boundaries are absorbing so fire stops at the edge of the matrix and does not wrap around to the opposite side.

Each cell can have one of three discrete states implemented using `IntEnum` for type safety and ease of reading:
- `VOID`  (0)
- `TREE` (1)
- `FIRE` (2)

### Update rules
The simulation runs on synchronous update rules meaning the entire matrix updates at each discrete time step ($t \to t+1$) according to four rules: 
1) **Propagation:** Each `FIRE` previously on the grid will spread to `TREE` in their Von Neumann neighborhood (4 orthogonal cells, no diagonals).
2) **Burnout:** Source `FIRE` burns down and is replaced by `VOID`.
3) **Lightning:** Remaining `TREE` cells spontaneously ignite into `FIRE` following lightning probability $f$.
4) **Growth:** `VOID` cells grow into `TREE` with probability $p$.

## Software architecture
### Vectorized NumPy 
Iterating over a 2D grid using nested `for` loops introduces heavy calculation overhead and is inherently slow. Instead, this program uses NumPy to compute array operations. It is significantly faster because NumPy methods are written in C, which allows for quick vectorized operations using boolean masking. Moreover, NumPy allows for efficient memory allocation by using `np.uint8` arrays.

In order to solve the toroidal wrap-around side effect of `np.roll()`, which would allow fire to jump from one edge of the grid to the other, static boolean boundary masks are pre-computed when the matrix is initialized and applied each time the grid is rolled.

### Code quality
To ensure proper modularity and code quality, this script is written using several core paradigms:
- **Separation of concerns:** The core mathematical engine (`Matrix`, `SimParam`, `Proba`, `State`) is strictly decoupled from terminal I/O (`enter_int`, `enter_proba`). This allows for fast, headless data collection and will facilitate porting the script to Project Mesa.
- **Safety measures:** To ensure reliable execution, the entire script is tested with `pytest`. It is strictly type-hinted and configuration parameters are rendered immutable via `@dataclass(frozen=True)`.
- **Maintainability:** The project delivers clean debugging feedback through structured `logging`. The modular architecture allows for standard developer installation and dependency management using `pyproject.toml`.

### Repository structure
```
forest-fire-model/
├── pyproject.toml
├── README.md
├── README_FR.md
├── src/
│   └── forest_fire/
│       ├── __init__.py
│       └── main.py
└── tests/
    └── test_main.py
```

## Installation
***Installation requires Python 3.10+ and git.***

---

### Linux and macOS
```bash
# 1. Clone the repository and enter the directory
git clone https://github.com/AngeleKowalik/forest_fire_model.git
cd forest_fire_model

# 2. Create and activate an isolated virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 3. Upgrade pip (recommended)
pip install --upgrade pip
```
4a. Standard installation (to simply run the simulation)
```bash
pip install .
```

4b. Developer installation (editable mode, testing and linting dependencies)
```bash
pip install -e ".[dev]"
```

### Windows
```powershell
# 1. Clone the repository and enter the directory
git clone https://github.com/AngeleKowalik/forest_fire_model.git
cd forest_fire_model

# 2. Create and activate an isolated virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# (Note: If you encounter an execution policy error, run: 
# Set-ExecutionPolicy Unrestricted -Scope CurrentUser)

# (Note: If using classic Command Prompt/cmd.exe, run:
# .\.venv\Scripts\activate.bat)

# 3. Upgrade pip (recommended)
python -m pip install --upgrade pip
```

4a. Standard installation (to simply run the simulation)
```powershell
pip install .
```

4b. Developer installation (editable mode, testing and linting dependencies)
```powershell
pip install -e ".[dev]"
```

## Usage
**Linux / macOS**
```bash
python3 -m forest_fire.main
```

**Windows**
```powershell
python -m forest_fire.main
```

Then follow the instructions written in the CLI

**Example:**
```bash
python3 -m forest_fire.main
# How many rows do you want in your matrix ?
4

# How many columns do you want in your matrix ?
5

# How many cycles should the program run for ?
5

# How many cycle should the program run for ?
6

# [0 0 1 0 0]
# [0 1 0 0 0]
# [1 1 0 0 0]
# [1 0 0 1 0]

# [0 0 1 0 0]
# [1 1 0 1 1]
# [1 1 0 0 1]
# [1 0 1 1 0]

# [1 1 1 0 0]
# [1 1 1 1 1]
# [1 1 0 0 1]
# [1 1 1 1 1]

# [1 1 1 0 0]
# [1 1 2 1 1]
# [1 1 0 0 1]
# [1 1 1 1 1]

# [1 1 2 0 0]
# [1 2 0 2 1]
# [1 1 1 0 1]
# [2 1 1 1 1]

# [1 2 0 0 0]
# [2 0 1 1 2]
# [2 2 1 0 1]
# [1 2 1 1 1]
```

## Testing
### Explanation
To ensure robust and true results, each mathematical function runs against an oracle. 

For the `Matrix.spread()`, those oracles are deterministic spatial tests hard-coded on a $3 \times 3$ matrix. Oracles are made for all critical starting points to prove that fire propagates orthogonally and never jumps across matrix's edges.

For `probabilistic_insert()`, edge cases such as 0 and 1 are tested independently. For other probabilities ranging from 0 excluded to 1 excluded, the test uses the Law of Large Numbers with $N = 10 000$ iterations to verify that the empirical mean converges within $\pm 0.01$ of the target probability.

### Execution
```bash
# Run all unit tests
pytest

# Run with verbose output (shows each individual test function name and status)
pytest -v

# Run a single specific test (e.g., only the top-left corner test)
pytest -k "test_top_left_corner"
```

## Roadmap
- [x] Writing a function for the user to enter float between 0 and 1 (for proba)
- [x] Creating tests using pytest for each function
- [x] Completing README.md
- [ ] Completing README_FR.md
- [ ] Implementing a safeguard system to protect from wrong hard coded values (using IntEnum)
- [ ] Implementing graphs using Matplotlib
- [ ] Adding a visualisation using pygame or similar library
- [ ] Storing results of each runs in an external file
- [ ] Porting the package to Project Mesa

## Fixes to make
- [x] Checking original paper to see the correct order of operation
- [x] Refactoring the spreading function to remove fire jumping from side to side of the matrix bug
- [x] Improving the slow python's loops by using NumPy methods instead





