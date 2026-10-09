
INITIAL = (1, 2, 3,
           0, 4, 6,
           7, 5, 8)

GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def get_neighbors(state):
    neighbors = []
    b = state.index(0)              
    row, col = divmod(b, 3)

    moves = [("Up", -1, 0), ("Down", 1, 0), ("Left", 0, -1), ("Right", 0, 1)]
    for name, dr, dc in moves:
        r, c = row + dr, col + dc
        if 0 <= r < 3 and 0 <= c < 3:     
            n = r * 3 + c
            new = list(state)
            new[b], new[n] = new[n], new[b]  
            neighbors.append((name, tuple(new)))
    return neighbors


def is_solvable(state):
   
    tiles = [x for x in state if x != 0]
    inv = sum(1 for i in range(len(tiles))
              for j in range(i + 1, len(tiles)) if tiles[i] > tiles[j])
    return inv % 2 == 0


def print_state(state):
    for i in range(0, 9, 3):
        print(" ".join(str(x) if x != 0 else "_" for x in state[i:i + 3]))
    print()



def depth_limited_search(state, goal, limit, path, on_path, counter):
    counter[0] += 1
    if state == goal:
        return path
    if limit == 0:
        return "cutoff"

    cutoff_occurred = False
    for move, nxt in get_neighbors(state):
        if nxt in on_path:                  
            continue
        on_path.add(nxt)
        result = depth_limited_search(nxt, goal, limit - 1, path + [move], on_path, counter)
        on_path.remove(nxt)                 

        if result == "cutoff":
            cutoff_occurred = True
        elif result is not None:
            return result                    
    return "cutoff" if cutoff_occurred else None


def ids(start, goal, max_depth=50):
    counter = [0]                            
    for depth in range(max_depth + 1):
        result = depth_limited_search(start, goal, depth, [], {start}, counter)
        print(f"  IDS depth limit {depth:2d} -> nodes so far: {counter[0]}")
        if result != "cutoff":
            return result, counter[0]       
    return None, counter[0]



def show_solution(start, path):
    state = start
    print("Initial state:")
    print_state(state)
    moves = {"Up": -3, "Down": 3, "Left": -1, "Right": 1}  
    for i, m in enumerate(path, 1):
        b = state.index(0)
        n = b + moves[m]
        s = list(state)
        s[b], s[n] = s[n], s[b]
        state = tuple(s)
        print(f"Step {i}: move blank {m}")
        print_state(state)



if __name__ == "__main__":
    if not is_solvable(INITIAL):
        print("This puzzle is not solvable.")
        raise SystemExit

    print("=== IDS ===")
    path, n = ids(INITIAL, GOAL)
    print(f"Solution length: {len(path)} moves, total nodes visited: {n}")
    print("Moves:", path, "\n")
    show_solution(INITIAL, path)