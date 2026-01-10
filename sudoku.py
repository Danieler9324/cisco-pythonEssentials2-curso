sudoku = []

for _ in range(9):
    row = input().strip()
    if len(row) != 9 or not row.isdigit():
        print("No")
        exit()
    sudoku.append(row)

digits = set("123456789")

for row in sudoku:
    if set(row) != digits:
        print("No")
        exit()

for col in range(9):
    column = {sudoku[row][col] for row in range(9)}
    if column != digits:
        print("No")
        exit()

for r in range(0, 9, 3):
    for c in range(0, 9, 3):
        block = set()
        for i in range(3):
            for j in range(3):
                block.add(sudoku[r + i][c + j])
        if block != digits:
            print("No")
            exit()

print("Si")
