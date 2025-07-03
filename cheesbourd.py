size = 8  # 8x8 chessboard

for row in range(size):
    for col in range(size):
        if (row + col) % 2 == 0:
            print("■", end=" ")
        else:
            print("□", end=" ")
    print()