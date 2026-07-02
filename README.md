# TIC-TIC-TOE
# Tic-Tac-Toe AI using Minimax with Alpha-Beta Pruning

## Overview

This project implements an intelligent **Tic-Tac-Toe** game simulation using the **Minimax algorithm** enhanced with **Alpha-Beta Pruning**. The program demonstrates how two rational AI agents play against each other optimally, ensuring the best possible outcome from every game state.

The implementation also traces the search process by displaying utility values, alpha-beta updates, and pruning events, making it an excellent educational project for understanding adversarial search algorithms in Artificial Intelligence.

---

## Features

* Full implementation of the **Minimax Algorithm**
* **Alpha-Beta Pruning** optimization to reduce unnecessary search
* Rational **MAX (X)** and **MIN (O)** AI agents
* Automatic game simulation with no human input required
* Real-time board visualization
* Search tree tracing
* Displays:

  * Utility values
  * Alpha (α) and Beta (β) updates
  * Alpha-Beta cutoff events
  * Number of pruned branches during each move
* Prefers:

  * Faster victories
  * Delayed defeats
* Detects:

  * Win
  * Loss
  * Draw

---

## Algorithm Used

### Minimax

The Minimax algorithm evaluates every possible future game state to determine the optimal move.

* **MAX Player (X):** Maximizes the utility score.
* **MIN Player (O):** Minimizes the utility score.

Both players assume their opponent always makes the best possible move.

---

### Alpha-Beta Pruning

Alpha-Beta Pruning improves the efficiency of Minimax by eliminating branches that cannot influence the final decision.

Benefits include:

* Reduced search space
* Faster decision making
* Same optimal result as standard Minimax

The implementation records the number of pruned branches after every move.

---

## Evaluation Function

The utility function scores terminal states as follows:

| Result |         Score |
| ------ | ------------: |
| X Wins |  `10 - depth` |
| O Wins | `-10 + depth` |
| Draw   |           `0` |

Using the search depth ensures:

* The AI chooses the quickest winning path.
* The AI postpones losing positions whenever possible.

---

## Project Structure

```
.
├── main.py
└── README.md
```

### Main Components

* `print_board()` – Displays the Tic-Tac-Toe board.
* `check_terminal()` – Detects wins, draws, and terminal states.
* `evaluate()` – Computes the utility value of terminal positions.
* `alpha_beta()` – Implements the Minimax algorithm with Alpha-Beta pruning.
* `simulate_game()` – Runs a complete AI vs AI game simulation.

---

## Requirements

* Python 3.8 or later

No external libraries are required.

---

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/your-username/tic-tac-toe-alpha-beta.git
```

2. Navigate to the project directory:

```bash
cd tic-tac-toe-alpha-beta
```

3. Run the program:

```bash
python main.py
```

---

## Sample Output

```
=== STARTING SIMULATION: RATIONAL MAX (X) vs RATIONAL MIN (O) ===

--- X's Turn ---

-> MAX evaluated index 0: Utility = 0 | α = 0, β = inf
-> MAX evaluated index 1: Utility = 0 | α = 0, β = inf
...

[MAX Agent] Chooses index 4 with guaranteed utility: 0

Total branches pruned during this search: 1523
```

The game continues until one player wins or both agents reach a perfectly played draw.

---

## Learning Objectives

This project demonstrates important Artificial Intelligence concepts including:

* Adversarial Search
* Game Trees
* Minimax Algorithm
* Alpha-Beta Pruning
* Utility Functions
* Optimal Decision Making
* Recursive Search
* State Space Exploration

---

## Time Complexity

| Algorithm                      | Complexity |
| ------------------------------ | ---------- |
| Minimax                        | O(b^d)     |
| Alpha-Beta Pruning (Best Case) | O(b^(d/2)) |

Where:

* **b** = branching factor
* **d** = depth of the search tree

Alpha-Beta Pruning significantly reduces the number of nodes explored compared to standard Minimax.

---

## Future Improvements

Potential enhancements include:

* Human vs AI gameplay
* Adjustable difficulty levels
* Graphical User Interface (GUI)
* Search tree visualization
* Move ordering heuristics
* Performance benchmarking
* Support for larger board sizes

---

## Author

**Student ID:** F24-0518

---

## License

This project is intended for educational and academic purposes.

<img width="449" height="433" alt="image" src="https://github.com/user-attachments/assets/2a758d3a-f07d-4f9e-9834-fe106475a0a7" />
<img width="575" height="404" alt="image" src="https://github.com/user-attachments/assets/dfe8def1-d0ce-4e37-993c-4985974de87b" />
<img width="419" height="431" alt="image" src="https://github.com/user-attachments/assets/c12de649-a234-4234-888a-ab04d8a029ff" />
<img width="443" height="414" alt="image" src="https://github.com/user-attachments/assets/4d28093a-a9bb-490d-b4c5-c17befd9231e" />
<img width="491" height="431" alt="image" src="https://github.com/user-attachments/assets/2b5fac5e-7a78-44c7-bc62-6ecf48f741e4" />
<img width="292" height="65" alt="image" src="https://github.com/user-attachments/assets/9b4e301c-b284-4792-91dc-9e7e551598a8" />




