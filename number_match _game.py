import random
import operator 

print("Welcome")
print("Welcome friends!")
print("Welcome to the Number Match Game!")
print("Find two matching numbers hidden in the grid!")

# Generate a 4x4 grid with pairs of numbers from 1 to 8
numbers = list(range(1, 9)) * 2
random.shuffle(numbers)
grid = [numbers[i:i + 4] for i in range(0, 16, 4)]

# Create a mask for revealed numbers
revealed = [[False]*4 for _ in range(4)]

def print_grid():
    for i in range(4):
        for j in range(4):
            if revealed[i][j]:
                print(f"{grid[i][j]:2}", end=" ")
            else:
                print(" *", end=" ")
        print()

def get_coords():
    while True:
        try:
            coords = input("Enter row and column (e.g. 1 2): ")
            row, col = map(int, coords.split())
            if 0 <= row < 4 and 0 <= col < 4 and not revealed[row][col]:
                return row, col
            else:
                print("Invalid coordinates or already revealed.")
        except:
            print("Please enter valid numbers.")

matches = 0
attempts = 0
while matches < 8:
    print_grid()
    print("Select the first number:")
    r1, c1 = get_coords()
    revealed[r1][c1] = True
    print_grid()
    print("Select the second number:")
    r2, c2 = get_coords()
    revealed[r2][c2] = True
    print_grid()
    attempts += 1

    if grid[r1][c1] == grid[r2][c2]:
        print("🎉 Match found!")
        matches += 1
    else:
        print("❌ No match.")
        revealed[r1][c1] = False
        revealed[r2][c2] = False

    input("Press Enter to continue...")

print(f"Congratulations! You found all pairs in {attempts} attempts.")
