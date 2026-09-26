# AI Search Algorithms Performance Evaluation

## Practical Title

Evaluate the performance of various algorithms (Uninformed, Informed, Local Search and Constraint Satisfaction) of problem solving through Search.

## Objective

The objective of this practical is to implement and compare different Artificial Intelligence search techniques:

* Breadth First Search (BFS)
* Depth First Search (DFS)
* A* Search
* Hill Climbing
* Backtracking for Constraint Satisfaction Problem

The algorithms are evaluated using parameters such as:

* Nodes expanded
* Solution cost
* Number of steps
* Recursive calls
* Execution time
* Solution validity

## Technologies Used

* Python 3
* VS Code / PyCharm
* Python Standard Library

## Python Libraries Used

The project uses only built-in Python libraries:

* `collections`
* `heapq`
* `time`
* `random`

No external Python packages are required.

## Algorithms Implemented

### 1. Breadth First Search

BFS explores the graph level by level using a queue.

### 2. Depth First Search

DFS explores one branch deeply before backtracking.

### 3. A* Search

A* is an informed search algorithm that uses:

```text
f(n) = g(n) + h(n)
```

where:

* `g(n)` is the actual path cost.
* `h(n)` is the heuristic cost.
* `f(n)` is the estimated total cost.

### 4. Hill Climbing

Hill Climbing is a local search algorithm. It continuously moves toward a neighboring state with fewer conflicts.

The algorithm is demonstrated using the 8-Queens problem.

### 5. Backtracking CSP

Backtracking is used to solve the 8-Queens Constraint Satisfaction Problem.

The algorithm places queens one by one and backtracks whenever a constraint is violated.

## Problems Used

### Graph Search

BFS, DFS and A* use a weighted graph.

```text
Start = A
Goal  = H
```

### 8-Queens

Hill Climbing and Backtracking use the 8-Queens problem.

The objective is to place 8 queens on an 8 × 8 chessboard so that no two queens attack each other.

## How to Run

### Step 1: Check Python

```bash
python --version
```

### Step 2: Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

### Step 3: Open the project

```bash
cd AI_Search_Practical
```

### Step 4: Run the program

```bash
python search_algorithms.py
```

No additional package installation is required.

## Sample Output

```text
=================================================================
AI SEARCH ALGORITHMS PERFORMANCE EVALUATION
=================================================================

BREADTH FIRST SEARCH
Path: A -> B -> E -> H
Cost: 11
Nodes Expanded: 8
Time: ... ms

DEPTH FIRST SEARCH
Path: A -> B -> D -> G -> H
Cost: 8
Nodes Expanded: ...
Time: ... ms

A* SEARCH
Path: A -> B -> D -> G -> H
Cost: 8
Nodes Expanded: ...
Time: ... ms

HILL CLIMBING
Solution: [...]
Conflicts: 0
Steps: ...
Random Restarts: ...
Time: ... ms

BACKTRACKING CSP
Solution: [...]
Conflicts: 0
Recursive Calls: ...
Time: ... ms
```

The execution time may vary depending on the computer and Python environment.

## Performance Parameters

| Algorithm     | Category          | Main Performance Measure      |
| ------------- | ----------------- | ----------------------------- |
| BFS           | Uninformed Search | Nodes Expanded                |
| DFS           | Uninformed Search | Nodes Expanded                |
| A*            | Informed Search   | Nodes Expanded and Path Cost  |
| Hill Climbing | Local Search      | Steps and Conflicts           |
| Backtracking  | CSP               | Recursive Calls and Conflicts |

## Results

The program successfully demonstrates five different AI problem-solving techniques.

BFS, DFS and A* solve the graph-search problem, while Hill Climbing and Backtracking solve the 8-Queens problem.

The program also measures the execution time of each algorithm.

## Conclusion

Different search algorithms behave differently depending on the problem structure.

BFS systematically explores states level by level. DFS explores states deeply. A* uses heuristic information to guide the search. Hill Climbing performs local optimization, while Backtracking is useful for Constraint Satisfaction Problems.

The practical demonstrates how search strategy affects solution cost, number of explored states and execution time.

## Author

Student Name: Dipti Patil

PRN: 202401040161

Branch: Computer Science Engineering

Division: C
