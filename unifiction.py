def is_var(x):
    return isinstance(x, str) and len(x) == 1 and x.islower()


def unify(x, y, subs):
    if x == y:
        return subs

    if is_var(x):
        subs[x] = y
        return subs

    if is_var(y):
        subs[y] = x
        return subs

    if isinstance(x, tuple) and isinstance(y, tuple):
        if x[0] != y[0] or len(x) != len(y):
            return None

        for a, b in zip(x[1:], y[1:]):
            subs = unify(a, b, subs)
            if subs is None:
                return None
        return subs

    return None


def parse(expr):
    expr = expr.strip()

    if '(' not in expr:
        return expr

    name, args = expr.split('(', 1)
    args = args[:-1]

    parts = []
    depth = 0
    start = 0

    for i, ch in enumerate(args):
        if ch == '(':
            depth += 1
        elif ch == ')':
            depth -= 1
        elif ch == ',' and depth == 0:
            parts.append(args[start:i].strip())
            start = i + 1

    parts.append(args[start:].strip())

    return (name.strip(), *[parse(a) for a in parts])


def unification(e1, e2):
    x = parse(e1)
    y = parse(e2)

    if not isinstance(x, tuple) or not isinstance(y, tuple):
        return "Unification Failed"

    if x[0] != y[0] or len(x) != len(y):
        return "Unification Failed"

    subs = unify(x, y, {})

    if subs is None:
        return "Unification Failed"

    return {k: apply_subs(v, subs) for k, v in subs.items()}


def apply_subs(term, subs):
    while is_var(term) and term in subs:
        term = subs[term]

    if isinstance(term, tuple):
        return tuple(apply_subs(x, subs) for x in term)

    return term



e1 = input("Enter first expression: ")
e2 = input("Enter second expression: ")

result = unification(e1, e2)

print("\nExpression 1:", e1)
print("Expression 2:", e2)

if result == "Unification Failed":
    print("Unification Failed")
else:
    print("Substitution:", result)
    print("Unification Successful")
