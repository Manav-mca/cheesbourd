import string

size = 8  # 8x8 chessboard
columns = string.ascii_uppercase[:size]

# Print column headers
print("  ", end="")
for col in columns:
    print(col, end=" ")
print()

for row in range(1, size + 1):
    print(row, end=" ")
    for col in range(size):
        if (row + col) % 2 == 0:
            print("■", end=" ")
        else:
            print("□", end=" ")
    print()
    
