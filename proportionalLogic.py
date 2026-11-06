
import itertools

def print_truth_table(query_name, query_fn):
    symbols = ['P', 'Q', 'R']
    headers = ['P', 'Q', 'R', 'Q -> P', 'P -> ~Q', 'Q v R', 'KB', query_name]

    print("\n=== Truth Table checking KB |= " + query_name + " ===")

    widths = [8, 8, 8, 10, 10, 10, 8, 12]

    header = " | ".join(headers[i].center(widths[i]) for i in range(len(headers)))
    print(header)
    print("-" * len(header))

    entails = True

    for values in itertools.product([False, True], repeat=3):
        m = dict(zip(symbols, values))

        s1 = not m['Q'] or m['P']
        s2 = not m['P'] or not m['Q']
        s3 = m['Q'] or m['R']

        kb = s1 and s2 and s3
        q_val = query_fn(m)

        row = [m['P'], m['Q'], m['R'], s1, s2, s3, kb, q_val]

        row_str = " | ".join(
            str(row[i]).lower().center(widths[i])
            for i in range(len(row))
        )

        if kb:
            row_str += "  <-- KB Model"
            if not q_val:
                entails = False

        print(row_str)

    print("\nKB entails " + query_name + " : " + str(entails))
    print()


print_truth_table("R", lambda m: m['R'])

print_truth_table("R -> P", lambda m: not m['R'] or m['P'])

print_truth_table("Q -> R", lambda m: not m['Q'] or m['R'])
