import heapq

GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def heuristic(state):
    distance = 0

    for i in range(9):
        tile = state[i]

        if tile != 0:
            goal_pos = tile - 1

            row1, col1 = divmod(i, 3)
            row2, col2 = divmod(goal_pos, 3)

            distance += abs(row1 - row2) + abs(col1 - col2)

    return distance


def get_neighbors(state):
    neighbors = []

    blank = state.index(0)
    row, col = divmod(blank, 3)

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
    open_list = [(heuristic(start), 0, start)]

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