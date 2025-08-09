def is_safe(m, c):  
    mr, cr = 3 - m, 3 - c
    return all(x >= 0 for x in [m, c, mr, cr]) and \
           (m == 0 or m >= c) and (mr == 0 or mr >= cr)
def display(m, c):
    print(f"\n{'M '*m + 'C '*c}|", end=' ')
    print("--- |", 'M '*(3-m) + 'C '*(3-c))
def game():
    print("\nGame Start\nRules:\n1. Max 2 on boat\n2. M >= C or M gets eaten\n3. Boat can’t travel empty")
    m, c, boat = 3, 3, 'left'
    while m or c:
        display(m, c)
        print("\nLeft -> Right" if boat == 'left' else "Right -> Left")
        try:
            move_m = int(input("Missionaries to travel => "))
            move_c = int(input("Cannibals to travel => "))
        except:
            print("Invalid input! Try again.")
            continue
        if not (1 <= move_m + move_c <= 2):
            print("Boat must carry 1 or 2 people!")
            continue
        nm, nc = (m - move_m, c - move_c) if boat == 'left' else (m + move_m, c + move_c)
        if not is_safe(nm, nc):
            print("Invalid move! Try again.")
            continue
        m, c, boat = nm, nc, 'right' if boat == 'left' else 'left'
    display(m, c)
    print("\n🎉 All crossed safely!")

game()
