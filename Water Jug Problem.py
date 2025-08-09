def water_jug_problem(jug1_capacity, jug2_capacity, target1, target2):
    visited = set()
    steps = []
    def pour(jug1, jug2):
        if jug1 == target1 and jug2 == target2:
            steps.append((jug1, jug2))
            return True
        if (jug1, jug2) in visited:
            return False
        visited.add((jug1, jug2))
        steps.append((jug1, jug2))
        if pour(jug1_capacity, jug2):
            return True
        if pour(jug1, jug2_capacity):
            return True
        pour_amt = min(jug1, jug2_capacity - jug2)
        if pour(jug1 - pour_amt, jug2 + pour_amt):
            return True
        pour_amt = min(jug2, jug1_capacity - jug1)
        if pour(jug1 + pour_amt, jug2 - pour_amt):
            return True
        if pour(0, jug2):
            return True
        if pour(jug1, 0):
            return True
        steps.pop()
        return False
    if pour(0, 0):
        print(f"Steps to reach Jug1: {target1}L and Jug2: {target2}L")
        for s in steps:
            print("Jug1:", s[0], "Liters, Jug2:", s[1], "Liters")
    else:
        print("No solution found.")
water_jug_problem(4, 3, 2, 3)
