from collections import deque
import heapq
import time
import random


# ---------------------------------------------------------
# Graph used for BFS, DFS and A*
# ---------------------------------------------------------

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 2)],
    'D': [('G', 3)],
    'E': [('G', 1), ('H', 5)],
    'F': [('G', 1), ('H', 4)],
    'G': [('H', 2)],
    'H': []
}


# Heuristic values for A*
heuristic = {
    'A': 8,
    'B': 7,
    'C': 5,
    'D': 5,
    'E': 3,
    'F': 3,
    'G': 2,
    'H': 0
}


# ---------------------------------------------------------
# Breadth First Search
# ---------------------------------------------------------

def bfs(start, goal):

    queue = deque([(start, [start], 0)])
    visited = {start}
    expanded = 0

    while queue:

        node, path, cost = queue.popleft()
        expanded += 1

        if node == goal:
            return path, cost, expanded

        for neighbour, weight in graph[node]:

            if neighbour not in visited:

                visited.add(neighbour)

                queue.append(
                    (
                        neighbour,
                        path + [neighbour],
                        cost + weight
                    )
                )

    return None, 0, expanded


# ---------------------------------------------------------
# Depth First Search
# ---------------------------------------------------------

def dfs(start, goal):

    stack = [(start, [start], 0)]
    visited = set()
    expanded = 0

    while stack:

        node, path, cost = stack.pop()

        if node in visited:
            continue

        visited.add(node)
        expanded += 1

        if node == goal:
            return path, cost, expanded

        for neighbour, weight in reversed(graph[node]):

            if neighbour not in visited:

                stack.append(
                    (
                        neighbour,
                        path + [neighbour],
                        cost + weight
                    )
                )

    return None, 0, expanded


# ---------------------------------------------------------
# A* Search
# ---------------------------------------------------------

def a_star(start, goal):

    priority_queue = [
        (heuristic[start], 0, start, [start])
    ]

    best_cost = {
        start: 0
    }

    expanded = 0

    while priority_queue:

        f, cost, node, path = heapq.heappop(priority_queue)

        if cost != best_cost.get(node):
            continue

        expanded += 1

        if node == goal:
            return path, cost, expanded

        for neighbour, weight in graph[node]:

            new_cost = cost + weight

            if new_cost < best_cost.get(
                neighbour,
                float('inf')
            ):

                best_cost[neighbour] = new_cost

                new_f = (
                    new_cost
                    + heuristic[neighbour]
                )

                heapq.heappush(
                    priority_queue,
                    (
                        new_f,
                        new_cost,
                        neighbour,
                        path + [neighbour]
                    )
                )

    return None, 0, expanded


# ---------------------------------------------------------
# N-Queens Conflict Function
# ---------------------------------------------------------

def conflicts(state):

    total = 0
    n = len(state)

    for i in range(n):

        for j in range(i + 1, n):

            same_row = state[i] == state[j]

            same_diagonal = (
                abs(state[i] - state[j])
                == abs(i - j)
            )

            if same_row or same_diagonal:
                total += 1

    return total


# ---------------------------------------------------------
# Hill Climbing with Random Restart
# ---------------------------------------------------------

def hill_climbing(
    n=8,
    max_restarts=100,
    seed=42
):

    random_generator = random.Random(seed)

    total_steps = 0

    for restart in range(max_restarts):

        state = [
            random_generator.randrange(n)
            for _ in range(n)
        ]

        for step in range(100):

            current_conflicts = conflicts(state)

            # Solution found
            if current_conflicts == 0:
                return (
                    state,
                    total_steps,
                    restart + 1
                )

            best_conflicts = current_conflicts
            best_moves = []

            # Check all neighbouring states
            for column in range(n):

                old_row = state[column]

                for row in range(n):

                    if row == old_row:
                        continue

                    state[column] = row

                    new_conflicts = conflicts(state)

                    if new_conflicts < best_conflicts:

                        best_conflicts = new_conflicts

                        best_moves = [
                            (column, row)
                        ]

                    elif (
                        new_conflicts == best_conflicts
                        and new_conflicts < current_conflicts
                    ):

                        best_moves.append(
                            (column, row)
                        )

                state[column] = old_row

            # No better neighbour
            if best_conflicts >= current_conflicts:
                break

            column, row = best_moves[0]

            state[column] = row

            total_steps += 1

    return None, total_steps, max_restarts


# ---------------------------------------------------------
# Backtracking CSP - N Queens
# ---------------------------------------------------------

def n_queens_backtracking(n=8):

    state = [-1] * n

    columns = set()
    diagonals1 = set()
    diagonals2 = set()

    recursive_calls = 0

    def solve(row):

        nonlocal recursive_calls

        recursive_calls += 1

        # All queens placed
        if row == n:
            return True

        for column in range(n):

            # Check column
            if column in columns:
                continue

            # Check main diagonal
            if row - column in diagonals1:
                continue

            # Check secondary diagonal
            if row + column in diagonals2:
                continue

            # Place queen
            state[row] = column

            columns.add(column)
            diagonals1.add(row - column)
            diagonals2.add(row + column)

            # Recursive call
            if solve(row + 1):
                return True

            # Backtrack
            columns.remove(column)
            diagonals1.remove(row - column)
            diagonals2.remove(row + column)

            state[row] = -1

        return False

    solve(0)

    return state, recursive_calls


# ---------------------------------------------------------
# Measure Execution Time
# ---------------------------------------------------------

def measure(function, *args):

    start_time = time.perf_counter()

    result = function(*args)

    end_time = time.perf_counter()

    execution_time = (
        end_time - start_time
    ) * 1000

    return result, execution_time


# ---------------------------------------------------------
# Main Program
# ---------------------------------------------------------

print("=" * 65)
print("AI SEARCH ALGORITHMS PERFORMANCE EVALUATION")
print("=" * 65)


# ---------------------------------------------------------
# BFS
# ---------------------------------------------------------

(bfs_result, bfs_time) = measure(
    bfs,
    'A',
    'H'
)

bfs_path, bfs_cost, bfs_nodes = bfs_result

print("\nBREADTH FIRST SEARCH")

print(
    "Path:",
    " -> ".join(bfs_path)
)

print("Cost:", bfs_cost)

print(
    "Nodes Expanded:",
    bfs_nodes
)

print(
    "Time: %.6f ms"
    % bfs_time
)


# ---------------------------------------------------------
# DFS
# ---------------------------------------------------------

(dfs_result, dfs_time) = measure(
    dfs,
    'A',
    'H'
)

dfs_path, dfs_cost, dfs_nodes = dfs_result

print("\nDEPTH FIRST SEARCH")

print(
    "Path:",
    " -> ".join(dfs_path)
)

print("Cost:", dfs_cost)

print(
    "Nodes Expanded:",
    dfs_nodes
)

print(
    "Time: %.6f ms"
    % dfs_time
)


# ---------------------------------------------------------
# A*
# ---------------------------------------------------------

(astar_result, astar_time) = measure(
    a_star,
    'A',
    'H'
)

astar_path, astar_cost, astar_nodes = astar_result

print("\nA* SEARCH")

print(
    "Path:",
    " -> ".join(astar_path)
)

print("Cost:", astar_cost)

print(
    "Nodes Expanded:",
    astar_nodes
)

print(
    "Time: %.6f ms"
    % astar_time
)


# ---------------------------------------------------------
# Hill Climbing
# ---------------------------------------------------------

(hill_result, hill_time) = measure(
    hill_climbing
)

hill_state, hill_steps, hill_restarts = hill_result

print("\nHILL CLIMBING")

if hill_state is not None:

    print(
        "Solution:",
        hill_state
    )

    print(
        "Conflicts:",
        conflicts(hill_state)
    )

else:

    print("Solution: Not Found")

    print("Conflicts: N/A")


print(
    "Steps:",
    hill_steps
)

print(
    "Random Restarts:",
    hill_restarts
)

print(
    "Time: %.6f ms"
    % hill_time
)


# ---------------------------------------------------------
# Backtracking CSP
# ---------------------------------------------------------

(csp_result, csp_time) = measure(
    n_queens_backtracking
)

csp_state, csp_calls = csp_result

print("\nBACKTRACKING CSP")

print(
    "Solution:",
    csp_state
)

print(
    "Conflicts:",
    conflicts(csp_state)
)

print(
    "Recursive Calls:",
    csp_calls
)

print(
    "Time: %.6f ms"
    % csp_time
)


# ---------------------------------------------------------
# Performance Summary
# ---------------------------------------------------------

print("\n" + "=" * 65)
print("PERFORMANCE SUMMARY")
print("=" * 65)

print(
    "\nBFS"
)

print(
    "Nodes =",
    bfs_nodes,
    ", Cost =",
    bfs_cost
)

print(
    "\nDFS"
)

print(
    "Nodes =",
    dfs_nodes,
    ", Cost =",
    dfs_cost
)

print(
    "\nA*"
)

print(
    "Nodes =",
    astar_nodes,
    ", Cost =",
    astar_cost
)

print(
    "\nHill Climbing"
)

print(
    "Steps =",
    hill_steps
)

if hill_state is not None:

    print(
        "Conflicts =",
        conflicts(hill_state)
    )

else:

    print(
        "Conflicts = N/A"
    )


print(
    "\nBacktracking"
)

print(
    "Calls =",
    csp_calls
)

print(
    "Conflicts =",
    conflicts(csp_state)
)

print("\n" + "=" * 65)