import random
rows, cols = 4, 4
room = [[1 for _ in range(cols)] for _ in range(rows)]
print("All the room are dirty")
print(room)
total_dirty = sum(sum(row) for row in room)
cleaned = 0
print("\nBefore cleaning the room I detect all of these random dirts")
print(room)
for i in range(rows):
    for j in range(cols):
        print(f"Vacuum in this location now, {i} {j}")
        if room[i][j] == 1:
            room[i][j] = 0
            cleaned += 1
            print(f"cleaned {i} {j}")
print("Room is clean now, Thanks for using : A.SAFARJI CLEANER")
print(room)
performance = (cleaned / total_dirty) * 100
print(f"performance= {performance:.2f} %")
