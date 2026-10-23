import heapq

GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def heuristic(state):
    count = 0

    for i in range(9):
        if state[i] != 0 and state[i] != GOAL[i]:
            count += 1

    return count


def get_neighbors(state):
    neighbors = []

    blank = state.index(0)
    row = blank // 3
    col = blank % 3

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_pos = new_row * 3 + new_col

            new_state = list(state)
            new_state[blank], new_state[new_pos] = (
                new_state[new_pos], new_state[blank]
            )

            neighbors.append(tuple(new_state))

    return neighbors


def astar(start):
    open_list = []
    heapq.heappush(open_list, (heuristic(start), 0, start))

    parent = {start: None}
    cost = {start: 0}
    closed = set()

    while open_list:
        f, g, state = heapq.heappop(open_list)

        if state in closed:
            continue

        if state == GOAL:
            path = []

            while state is not None:
                path.append(state)
                state = parent[state]

            return path[::-1]

        closed.add(state)

        for neighbor in get_neighbors(state):
            new_g = g + 1

            if neighbor not in cost or new_g < cost[neighbor]:
                cost[neighbor] = new_g
                parent[neighbor] = state

                h = heuristic(neighbor)
                new_f = new_g + h

                heapq.heappush(
                    open_list, (new_f, new_g, neighbor)
                )

    return None


def display_state(state):
    for i in range(0, 9, 3):
        print(state[i:i + 3])


# Initial state: exactly four moves from the goal
start = (1, 2, 3,
         5, 0, 6,
         4, 7, 8)

path = astar(start)

if path:
    print("Solution found!")
    print("Total moves:", len(path) - 1)

    for step, state in enumerate(path):
        g = step
        h = heuristic(state)
        f = g + h

        print("\nStep:", step)
        display_state(state)
        print("g(n) =", g)
        print("h(n) =", h)
        print("f(n) =", f)

else:
    print("Solution not found.")