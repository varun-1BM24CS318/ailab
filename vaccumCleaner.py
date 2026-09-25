import random

def simple_reflex_agent():
    print("\n--- SIMPLE REFLEX AGENT ---")
    locations = ["A", "B"]
    status = {"A": random.choice(["Clean", "Dirty"]),
              "B": random.choice(["Clean", "Dirty"])}
    current_location = random.choice(locations)

    print(f"Initial state -> A: {status['A']}, B: {status['B']}, Vacuum at: {current_location}")

    steps = 0
    max_steps = 10  

    while steps < max_steps:
        percept = (current_location, status[current_location])
        print(f"\nStep {steps+1}: Percept = {percept}")

        if percept[1] == "Dirty":
            print(f"Action: Suck (cleaning {current_location})")
            status[current_location] = "Clean"
        elif current_location == "A":
            print("Action: Move Right")
            current_location = "B"
        elif current_location == "B":
            print("Action: Move Left")
            current_location = "A"

        print(f"State -> A: {status['A']}, B: {status['B']}, Vacuum at: {current_location}")
        steps += 1

        if status["A"] == "Clean" and status["B"] == "Clean":
            print("\nBoth rooms happen to be clean now (agent doesn't know/check this).")
            break

    print(f"\nReflex agent finished after {steps} steps (no explicit goal check).")


def goal_based_agent():
    print("\n--- GOAL-BASED AGENT ---")
    status = {"A": random.choice(["Clean", "Dirty"]),
              "B": random.choice(["Clean", "Dirty"])}
    current_location = random.choice(["A", "B"])

    print(f"Initial state -> A: {status['A']}, B: {status['B']}, Vacuum at: {current_location}")

    steps = 0

    def goal_achieved():
        return status["A"] == "Clean" and status["B"] == "Clean"

    while not goal_achieved():
        steps += 1
        print(f"\nStep {steps}: Vacuum at {current_location}, Status: {status[current_location]}")

        if status[current_location] == "Dirty":
            print(f"Action: Suck (cleaning {current_location})")
            status[current_location] = "Clean"
        else:
            current_location = "B" if current_location == "A" else "A"
            print(f"Action: Move to {current_location}")

        print(f"State -> A: {status['A']}, B: {status['B']}")

    print(f"\nGoal achieved in {steps} steps! Both rooms are clean.")


if __name__ == "__main__":
    simple_reflex_agent()
    goal_based_agent()